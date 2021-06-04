from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from UserAuth.models import User
import sqlite3 as sql
from UserAuth.forms import RegistrationForm, LogInForm, NewUserAccountForm, ProfileForm
from django.views.decorators.http import require_http_methods
from django.urls import reverse
import datetime

# Create your views here.

URLHOST = 'http://127.0.0.1:8000/'

def database(database,query,params):
    try:
        with sql.connect(database) as con:
            cur = con.cursor()
            if params:
                cur.execute(query,params)
                result = cur.fetchone()
            else:
                cur.execute(query)
                result = cur.fetchone()
    except TypeError as t:
        raise TypeError(t)
    except ConnectionRefusedError as e:
        raise ConnectionRefusedError(e)
    return result

@require_http_methods("POST")
def database_check(response):
    form = RegistrationForm(response.POST)
    if form.is_valid():
        email = form.cleaned_data["email"]
        has_email = database('db.sqlite3',"SELECT user_email FROM User WHERE user_email = ?;",(email,))
        logged_in = None
        if has_email:
            logged_in = database('db.sqlite3',"SELECT logged_in FROM User WHERE user_email = ?;",(email,))
        if not logged_in:
            return HttpResponseRedirect(URLHOST+'register/login')
        else:
            response.session['email'] = email
            return HttpResponseRedirect(URLHOST+'register/register/')

def forum(request):
    form = RegistrationForm
    context_vars = {'form': form,'heading':'Please fill out the form below','method':'post','action':'/register/sign-in/','val':'Next'}
    return render(request,'UserAuth/Sign In.html', context_vars)

def create_user_account(response):
    if response.method == "POST":
        form = NewUserAccountForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            name = "{} {}".format(form.cleaned_data["first_name"],form.cleaned_data["last_name"])
            username = form.cleaned_data["user_name"]
            date_of_birth = form.cleaned_data["date_of_birth"]
            if password1 == password2:
                u = User(user_name=name,user_username=username,user_email=email,user_password=password1,user_birth_date=date_of_birth,logged_in=True)
                u.save()
                return HttpResponseRedirect('register/profile/')
            else:
                form = NewUserAccountForm()
                heading = "The passwords do not match. Try again."
                context_vars = {'form':form,'heading':heading,'val':'CREATE ACCOUNT'}
                return render(response,"UserAuth/new_user_account.html",context_vars)
    elif response.method == "GET":
        email = response.session['email']
        form = NewUserAccountForm(initial={'email':email})
        context_vars = {'method':'post','action':'/register/register/','form':form,'heading':'Welcome to my Chess Website! Please create your account here.','val':'CREATE ACCOUNT'}
        return render(response,'UserAuth/new_user_account.html',context_vars)
    else:
        return HttpResponseNotAllowed(['GET','POST'])

@require_http_methods(["POST","GET"])
def login(response):
    if response.method == "POST":
        form = LogInForm(response.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            data = tuple(database('db.sqlite3',"SELECT user_email, user_password FROM User WHERE user_email = '"+email+"' and user_password = '"+password+"';"))
            if data != None:
                data_email = data[0]
                data_password = data[1]
            if data_email == email and data_password == password:
                database('db.sqlite3',"UPDATE User SET logged_in = True WHERE user_email = '"+email+"' and user_password = '"+password+"';")
                return HttpResponse("You have successfully logged into your account!")
            else:
                if data == None:
                    return HttpResponseRedirect('/register/register/')
                elif password != data_password:
                    context_vars = {'form':form,'heading':'The passwords do not match.','method':'post','action':'/register/login/','val':'Login'}
                    return render(response,'UserAuth/login.html',context_vars)
    else:
        form = LogInForm()
        context_vars = {'form':form,'heading':'Please sign in to your account here.','action':'/register/login/','method':'post','val':'Login'}
        return render(response,'UserAuth/login.html',context_vars)

@require_http_methods(["POST","GET"])
def profile(response):
    if response.method == 'POST':
        form = ProfileForm(response.post)
        if form.is_valid():
            email = response.session['email']
            pin = form.cleaned_data['pin']
            database('db.sqlite3',"UPDATE User SET security_pin = '"+pin+"' WHERE user_email = '"+email+"';")
            return HttpResponseRedirect('/settings/')
    else:
        email = response.session['email']
        form = ProfileForm(initial={'email':email})
        context_vars = {'form':form}
        return render(response,"UserAuth/profile.html",context_vars)