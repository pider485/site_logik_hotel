from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404
from reservation.forms import BookingForm
from reservation.models import Room,TypeRoom,Reservation

# Create your views here.
def room_list(request):
    rooms = Room.objects.all()
    context = {
        'message': 'passwor:123',
        'rooms' : rooms,
    }
    return render(request, template_name='room_list.html', context=context)
@login_required
def booking(request,id_room):
    room = get_object_or_404(Room,id = id_room)
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.reservator = request.user
            reservation.save()
    context = {
        'room' : room,
        'form' : form
    }
    return render(request, template_name='booking.html', context=context)