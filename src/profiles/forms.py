from django import forms


from .models import UserAccount

class UserAccountForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'FIRST NAME'}))
    last_name = forms.CharField(max_length=100,
                           widget= forms.TextInput
                           (attrs={'placeholder':'LAST NAME'}))
    account_email=forms.EmailField(max_length=256,
                           widget= forms.TextInput
                           (attrs={'placeholder':'EMAIL'}))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder':'PASSWORD'})
                           )
    confirm_password=forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'placeholder':'CONFIRM PASWORD'}))
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

    def clean_password(self, *args, **kwargs):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords must match.", code=1)
        else:
            return password