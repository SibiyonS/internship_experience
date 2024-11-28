from django.urls import path
from . import views
from .views import email_database

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
]
