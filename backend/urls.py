from . import views
from . views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard', views.dashboard, 'dashboard')
]
