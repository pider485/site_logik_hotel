# urls.py
from django.urls import path
from .views import room_list ,booking

urlpatterns = [
    path('', room_list, name='room_list'),
    path('booking/<int:id_room>', booking, name='booking')
]