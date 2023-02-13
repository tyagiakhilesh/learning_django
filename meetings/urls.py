from django.urls import path
from .views import details, all_rooms

urlpatterns = [
    path('<int:id>', details, name='meeting_detail'),
    path('rooms', all_rooms, name='all_rooms')
]
