from django.shortcuts import render
from django.http import Http404 
#can use getobjector404 and skip try except block

def home_view(request, *args, **kwargs):
    print(request)
    return render(request, "home.html", {})