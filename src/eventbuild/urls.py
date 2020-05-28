from django.urls import path

from eventbuild.views import event_home

urlpatterns = [
    path('', event_home, name="eventhome")
]