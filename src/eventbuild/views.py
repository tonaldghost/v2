from django.shortcuts import render

def event_home(request):
    """send to event home where events can be made and added to at the click of a button.
    The process is generate event and enter name. Apply add ons quickly for specific event types.
    Main challenge will be the models and creating and adding to them easily.
    Will need to make sure any new models have fields that can be left as null.
    Also check they are called correctly from buttons to and from JS and Python code."""
    return render(request, 'event-templates/event-home.html', {})
