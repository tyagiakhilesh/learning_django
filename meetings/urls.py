from django.urls import path
from .views import details, all_rooms, new

urlpatterns = [
    path('<int:id>', details, name='meeting_detail'),
    path('rooms', all_rooms, name='all_rooms'),
    path('new', new, name='new_meeting')
]
