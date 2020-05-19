from django.contrib import admin
from django.urls import path

from pages.views import home_view
from profiles.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('register', register, name='register'),
]
