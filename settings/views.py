from django.shortcuts import render, redirect
from authentication.forms import ProfileForm
from Chess.utils import database
from django.http import HttpResponseNotAllowed, HttpResponse

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


def settings(response):
    email = response.session['email']
    data = database(
        'db.SQLite3', 'FROM Settings SELECT * WHERE user.email = ?;', (email,))
    return HttpResponse(data)
