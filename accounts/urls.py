

from django.urls import path
from .views.auth import handle_login, handle_register, handle_logout, handle_profile
urlpatterns = [
    path('login/', handle_login, name='login'),
    path('register/', handle_register, name='register'),
    path('logout/', handle_logout, name='logout'),
    path('profile/', handle_profile, name='profile')

] 
