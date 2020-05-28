from django.shortcuts import render
# from django.http import Http404
#can use getobjector404 and skip try except block

def home_view(request):
    """sends user to home page"""
    return render(request, "home.html", {})

def insights_home_view(request):
    """sends user to insights home page"""
    return render(request, "insights/insights.html", {})
