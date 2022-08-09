import datetime
from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from authentication.models import User
from authentication.forms import RegistrationForm, LogInForm, NewUserAccountForm, ProfileForm
from django.views.decorators.http import require_http_methods
from django.urls import reverse
from accessigames.utils import database
from django.utils import timezone as tz
from datetime import date

# Create your views here.


@require_http_methods(['GET'])
def authentication_method_chooser(response):
    return render(response, 'authentication/choose_login_method.html')


@require_http_methods("POST")
def database_check(response):
    form = RegistrationForm(response.POST)
    if form.is_valid():
        email = form.cleaned_data["email"]
        has_email = database(
            'db.sqlite3', "SELECT email FROM User WHERE email = ?;", (email,))
        logged_in = None
        if has_email:
            logged_in = database(
                'db.sqlite3', "SELECT logged_in FROM User WHERE email = ?;", (email,))
        if not logged_in:
            return redirect('authentication:login')
        else:
            response.session['email'] = email
            return redirect('authentication:register')


def forum(request):
    form = RegistrationForm
    context_vars = {'form': form, 'heading': 'Please fill out the form below',
                    'method': 'post', 'action': '/register/database-check-in/', 'val': 'Next'}
    return render(request, 'authentication/Sign_In.html', context_vars)


def create_user_account(response):
    if response.method == "POST":
        form = NewUserAccountForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            first_name, last_name = form.cleaned_data['first_name'], form.cleaned_data['last_name']
            username = form.cleaned_data["user_name"]
            date_of_birth = response.POST['birth_date']
            if password1 == password2:
                u = User(first_name=first_name, last_name=last_name, username=username, email=email,
                         password=password1, birth_date=date_of_birth, logged_in=True)
                u.save()
                return redirect('authentication:profile')
            else:
                form = NewUserAccountForm()
                heading = "The passwords do not match. Try again."
                context_vars = {'form': form,
                                'heading': heading, 'val': 'CREATE ACCOUNT'}
                return render(response, "authenticationh/new_user_account.html", context_vars)
    elif response.method == "GET":
        email = response.session.get('email', None)
        form = NewUserAccountForm(initial={'email': email})
        min_date = tz.localtime(tz.now()).date()
        min_year = min_date.year-100
        context_vars = {'method': 'post', 'action': '/register/register/', 'form': form,
                        'heading': 'Welcome to my Chess Website! Please create your account here.', 'val': 'CREATE ACCOUNT', 'max': tz.localtime(tz.now()).date(), 'min': datetime.date(min_year, min_date.month, min_date.day), 'date_val': date(tz.localtime(tz.now()).date().year, 1, 1), 'date': True}
        return render(response, 'authentication/new_user_account.html', context_vars)
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@require_http_methods(["POST", "GET"])
def login(response):
    if response.method == "POST":
        form = LogInForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            data_email = None
            data_password = None
            data = database(
                'db.sqlite3', "SELECT email, password FROM User WHERE email = ? and password = ?;", (email, password))
            if data != None:
                data_email = data[0]
                data_password = data[1]
            if data_email == email and data_password == password:
                database(
                    'db.sqlite3', "UPDATE User SET logged_in = True WHERE email = ? and password = ?;", (email, password))
                return redirect('authentication:profile')
            else:
                if data == None:
                    return redirect('authentication:register')
                elif password != data_password:
                    context_vars = {'form': form, 'heading': 'The passwords do not match.',
                                    'method': 'post', 'action': '/register/login/', 'val': 'Login'}
                    return render(response, 'authentication/login.html', context_vars)
    else:
        form = LogInForm()
        context_vars = {'form': form, 'heading': 'Please sign in to your account here.',
                        'action': '/register/login/', 'method': 'post', 'val': 'Login'}
        return render(response, 'authentication/login.html', context_vars)


@require_http_methods(["POST", "GET"])
def profile(response):
    if response.method == 'POST':
        form = ProfileForm(response.post)
        if form.is_valid():
            if response.user.is_authenticated:
                email = response.user.email
                pin = form.cleaned_data['pin']
                database(
                    'db.sqlite3', "UPDATE User SET security_pin = ? WHERE email = ?;", (str(pin), email))
                return redirect('settings:')
            else:
                return HttpResponseForbidden()
    else:
        if response.user.is_authenticated:
            email = response.user.email
            form = ProfileForm(initial={'email': email})
            context_vars = {'form': form}
            return render(response, "authentication/profile.html", context_vars)
        else:
            return HttpResponseForbidden()
