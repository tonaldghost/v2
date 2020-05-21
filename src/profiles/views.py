from django.shortcuts import render, redirect
from django.contrib import messages
from smtp.smtpmail import account_mail_sender
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'You should receive an email shortly to confirm your account.')
            # email = form.cleaned_data['account_email']
            # account_mail_sender(email, "confirmation")
            return redirect('home') #eventually redirect to thanks page with message about confirming email
    
    else:
        form = UserRegisterForm()
    
    return render(request, 'registration/register_user.html', {'form':form})