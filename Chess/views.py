import os
from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponseNotAllowed,Http404,HttpResponse, FileResponse, response

# Create your views here.

def downloads(request):
    return render(request,'game/downloads.html')

def resources(request: HttpRequest):
    filename = request.GET.get('file')
    return FileResponse(open(os.path.join('GamingScripts','chess.exe'),'rb'),status)