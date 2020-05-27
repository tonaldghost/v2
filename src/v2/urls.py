from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.contrib.auth import views as auth_views
from pages.views import home_view
from profiles.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('register', register, name='register'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]

#refactor out the urls that should be in the specific app they belong too
