from django.shortcuts import render, redirect
from django.contrib import messages
from smtp.smtpmail import account_mail_sender
from .forms import UserRegisterForm

def register(request):
    """register function allows both get and post requests and currently
    only has a single form which is passed directly to the render method.
    Future work would include styling the form and errors better."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(
                request, f'You should receive an email at {email} shortly to confirm your account.')
            account_mail_sender(email, "confirmation")
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'registration/register_user.html', {'form': form})
