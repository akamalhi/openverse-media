
from django.urls import path
from .views import search_view, profile_view, delete_search_view

urlpatterns = [
    path('', search_view, name='search_media'),
        path('profile/', profile_view, name='profile'),
    path('delete-search/<int:search_id>/', delete_search_view, name='delete_search'),


] 