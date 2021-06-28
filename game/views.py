from django.shortcuts import render, get_object_or_404
from .models import Game
from UserAuth.models import User
from .forms import JoinGameForm
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponseNotAllowed,Http404,HttpResponse
from .GamingScripts.Chess.game import main

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
        return render(request,'game/game.html',{'game':main,'u1':users[0],'u2':users[1],'color1':(0,0,0),'color2':(255,255,255)})
    elif len(game.members.objects.all()) == 0:
        if not request.session.exists(request.session.get('email')):
            request.session['email'] = ''
        u = User.objects.filter(email=request.session['email']).first()
        u.game = game
        u.save(update_fields=['game'])
        return HttpResponse('Please wait for another player to join the game.')