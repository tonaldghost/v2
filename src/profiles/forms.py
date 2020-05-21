from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """Model form for registering new users. Attrs in the widget are for placeholders."""
    first_name = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput
                                (attrs={'placeholder':'FIRST NAME'}))
    last_name = forms.CharField(max_length=100, required=True,
                                widget=forms.TextInput
                                (attrs={'placeholder':'LAST NAME'}))
    email = forms.EmailField(max_length=256, required=True,
                                widget=forms.TextInput
                                (attrs={'placeholder':'EMAIL'}))
    password1 = forms.CharField(max_length=128, required=True,
                                widget=forms.PasswordInput
                                (attrs={'placeholder':'PASSWORD'}))
    password2 = forms.CharField(max_length=128, required=True,
                                widget=forms.PasswordInput
                                (attrs={'placeholder':'CONFIRM PASWORD'}))

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]
