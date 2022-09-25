from datetime import datetime

from django.shortcuts import render
from .models import Post

# Post variable will be a list with dictionaries inside.
# Use dictionaries like author and title in the home.html file.

date_now = datetime.now()
formatted_date = date_now.strftime("%d/%m/%Y")


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def register(request):
    return render(request, 'users/register.html')
