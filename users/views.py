from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Once user fills in the form and hits submit.
            # Create and save user data as a database object.
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('blog-home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})