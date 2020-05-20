from django import forms
from .models import UserAccount

class UserAccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = UserAccount
        fields = [
            'first_name',
            'last_name',
            'country',
            'account_email',
            'password'
        ]

    #check account does not exist already - throw validation error and handle it
    
    def clean(self):
        cleaned_data = super(UserAccountForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        # account_email = cleaned_data.get("account_email")

        if password != confirm_password:
            raise forms.ValidationError(
                'Passwords do not match.',
                code='1')
        
        return cleaned_data