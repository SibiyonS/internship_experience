from django.urls import path
from .views import download_database
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('download-db/', download_database, name='download_database'),
]
