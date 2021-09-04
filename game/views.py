from django.shortcuts import render, get_object_or_404
from .models import Game
from authentication.models import User
from .forms import JoinGameForm
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponseNotAllowed,Http404,HttpResponse, FileResponse, response

# Create your views here.

def join_game(response):
    if response.method == 'POST':
        form = JoinGameForm(data=response.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            game = Game.objects.filter(code=code)
            if game.exists():
                return HttpResponseRedirect('/game/'+game.first().code)
            else:
                return HttpResponseNotFound('That code does not exist.')
    elif response.method == 'GET':
        form = JoinGameForm()
        return render(response,'game/join_game.html',{'form':form})
    return HttpResponseNotAllowed(['GET','POST'])

def game(request,code):
    game = get_object_or_404(Game,code=code)
    if len(game.members.objects.all()) == 2:
        return HttpResponse("There are already two people playing in this game room.")
    elif len(game.members.objects.all()) == 1:
        if not request.session.exists(request.session.get('email')):
            request.session['email'] = ''
        u = User.objects.filter(email=request.session['email']).first()
        u.game = game
        u.save(update_fields=['game'])
        users = User.objects.filter(game=game)
        response = FileResponse(open('GamingScripts/chess.exe'))
        return render(request,'game/.html',{'game':response})
    elif len(game.members.objects.all()) == 0:
        if not request.session.exists(request.session.get('email')):
            request.session['email'] = ''
        u = User.objects.filter(email=request.session['email']).first()
        u.game = game
        u.save(update_fields=['game'])
        return HttpResponse('Please wait for another player to join the game.')