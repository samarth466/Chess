from django.shortcuts import render
from authentication.forms import ProfileForm
from chess.utils import database
from django.http import HttpResponse, HttpResponseNotAllowed, HttpRequest

# Create your views here.


def root(response):
    if response.method == "POST":
        pin = response.POST.get('pin')
        data_pin = database(
            'db.sqlite3', "SELECT security_pin FROM User WHERE security_pin = '"+pin+"';")
        email = database(
            'db.sqlite3', "SELECT user_email FROM  USER WHERE security_pin = '"+pin+"';")
        if data_pin:
            data = database(
                'db.sqlite3', "SELECT * FROM Settings WHERE user.user_email = '"+email+"';")
            context_vars = {'form': False}
            return HttpResponse(data)
    elif response.method == "GET":
        context_vars = {'form': True}
        return render(response, 'settings/form.html', context_vars)
