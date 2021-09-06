from django.shortcuts import render, redirect
from authentication.forms import ProfileForm
from Chess.utils import database
from django.http import HttpResponseNotAllowed, HttpResponse
from django.http import HttpResponse, HttpResponseForbidden

# Create your views here.


def root(response, email):
    response.session['email'] = email
    if response.method == "POST":
        pin = response.POST.get('pin')
        data_pin = database(
            'db.sqlite3', "SELECT security_pin FROM User WHERE email = ?;", (email,))
        if data_pin == pin and None not in (data_pin, pin):
            context_vars = {'form': False}
            return render(response, 'settings/form.html', context_vars)
    elif response.method == "GET":
        context_vars = {'form': True}
        return render(response, 'settings/form.html', context_vars)


def settings(request):
    if request.user.is_authenticated:
        data = database('db.SQLite3',"SELECT * FROM settings WHERE user.email = ?;",(request.user.email,))
        return HttpResponse(data)
    else:
        return HttpResponseForbidden()