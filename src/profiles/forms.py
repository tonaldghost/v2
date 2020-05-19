from django import forms
from .models import UserAccount

class UserAccountForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = [
            'first_name',
            'last_name',
            'account_email',
            'country'
        ]