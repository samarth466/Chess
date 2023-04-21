import datetime
from django.http.response import HttpResponseForbidden
from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from authentication.models import User
from authentication.forms import RegistrationForm, LogInForm, NewUserAccountForm, ProfileForm
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.utils import timezone as tz
from datetime import date

# Create your views here.


@require_safe
def authentication_method_chooser(response):
    return render(response, 'authentication/choose_login_method.html', {'next': response.GET.get('next')})


@require_POST
def database_check(response):
    form = RegistrationForm(response.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        try:
            if User.objects.get(email=email):
                return redirect('/register/login/?next='+response.GET.get('next'))
        except User.DoesNotExist:
            msg = f"{email} does not exist."
            return render(response, "authentication/error.html", {'error': msg, 'next': response.GET['next']})


@require_safe
def forum(request):
    form = RegistrationForm
    context_vars = {'form': form, 'heading': 'Please fill out the form below',
                    'method': 'post', 'action': '/register/database-check-in/?next='+request.GET['next'], 'val': 'Next'}
    return render(request, 'authentication/Sign_In.html', context_vars)


@require_http_methods(['POST', 'GET'])
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
                u = User(first_name=first_name, last_name=last_name, username=username,
                         email=email, birth_date=date_of_birth, logged_in=True)
                u.set_password(password1)
                u.save()
                login(response)
                if response.GET['next']:
                    return redirect(response.GET['next'])
                return redirect('blogs:home')
            else:
                form = NewUserAccountForm()
                heading = "The passwords do not match. Try again."
                context_vars = {'form': form,
                                'heading': heading, 'val': 'CREATE ACCOUNT'}
                return render(response, "authenticationh/new_user_account.html", context_vars)
    else:
        form = NewUserAccountForm()
        min_date = tz.localtime(tz.now()).date()
        min_year = min_date.year-100
        context_vars = {'method': 'post', 'action': '/register/register/?next='+response.GET['next'], 'form': form,
                        'heading': 'Welcome to my Chess Website! Please create your account here.', 'val': 'CREATE ACCOUNT', 'max': tz.localtime(tz.now()).date(), 'min': datetime.date(min_year, min_date.month, min_date.day), 'date_val': date(tz.localtime(tz.now()).date().year, 1, 1), 'date': True}
        return render(response, 'authentication/new_user_account.html', context_vars)


@require_http_methods(["POST", "GET"])
def login(response):
    if response.method == "POST":
        form = LogInForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(response, email=email, password=password)
            if user:
                login(response)
                if response.GET['next']:
                    return redirect(response.GET['next'])
                return redirect('blogs:home')
            else:
                return redirect(reverse('register')+'?next='+response.GET['next'])
    else:
        form = LogInForm()
        context_vars = {'form': form, 'heading': 'Please sign in to your account here.',
                        'action': '/register/login/?next='+response.GET['next'], 'method': 'post', 'val': 'Login'}
        return render(response, 'authentication/login.html', context_vars)


#require_http_methods(["POST", "GET"])
# def profile(response):
    # if response.method == 'POST':
        #form = ProfileForm(response.post)
        # if form.is_valid():
        # if response.user.is_authenticated:
        #email = response.user.email
        #pin = form.cleaned_data['pin']
        # database(
        # 'AccessiGames.sqlite3', "UPDATE User SET security_pin = ? WHERE email = ?;", (str(pin), email))
        # return redirect('settings:')
        # else:
        # return HttpResponseForbidden()
    # else:
        # if response.user.is_authenticated:
        #email = response.user.email
        #form = ProfileForm(initial={'email': email})
        #context_vars = {'form': form}
        # return render(response, "authentication/profile.html", context_vars)
        # else:
        # return HttpResponseForbidden()


@login_required
def logout(request):
    logout(request)
