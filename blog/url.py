from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('register/', views.register, name='register'),
    path('login/', views.register, name='login')
]
