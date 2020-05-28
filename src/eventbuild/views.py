from django.shortcuts import render

def event_home(request):
    """send to event home"""
    return render(request, 'event-templates/event-home.html', {})
