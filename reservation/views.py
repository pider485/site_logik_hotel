from django.shortcuts import render
from reservation.models import Room,TypeRoom,Reservation

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()
    context = {
        'message': 'passwor:123',
        'rooms' : rooms,
    }
    return render(request, template_name='room_list.html', context=context)