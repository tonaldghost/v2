from django import forms

from .models import UserAccount

class UserAccountForm(forms.ModelForm):
    """Model form for registering new users. Attrs in the widget are for placeholders."""
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput
                                 (attrs={'placeholder':'FIRST NAME'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput
                                (attrs={'placeholder':'LAST NAME'}))
    account_email = forms.EmailField(max_length=256,
                                widget=forms.TextInput
                                (attrs={'placeholder':'EMAIL'}))
    password = forms.CharField(max_length=128, 
                                widget=forms.PasswordInput
                                (attrs={'placeholder':'PASSWORD'}))
    confirm_password = forms.CharField(max_length=128, 
                                widget=forms.PasswordInput
                                (attrs={'placeholder':'CONFIRM PASWORD'}))
    class Meta:
        model = UserAccount
        fields = [
            'first_name',
            'last_name',
            'country',
            'account_email',
            'password'
        ]

    def clean_email(self):
        """checks user does not already exist in db"""
        account_email = self.cleaned_data.get('account_email')

        try:
            UserAccount.objects.get(account_email=account_email)
        except UserAccount.DoesNotExist:
            return account_email

        raise forms.ValidationError('An account with this email already exists.')

    def clean_password(self):
        """checks users passwords match in form and renders error if not"""
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("Passwords must match.")

        return password
