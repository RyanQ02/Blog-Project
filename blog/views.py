from datetime import datetime

from django.shortcuts import render

# Post variable will be a list with dictionaries inside.
# Use dictionaries like author and title in the home.html file.

date_now = datetime.now()
formatted_date = date_now.strftime("%d/%m/%Y")

posts = [
    {
        'author': 'Ryan',
        'title': 'Blog Post 1',
        'content': 'First Post!',
        'date_posted': formatted_date,
    },
    {
        'author': 'Jason',
        'title': 'Blog Post 2',
        'content': 'Second Post!',
        'date_posted': formatted_date,
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
