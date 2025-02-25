from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Room, RoomBooking
from .forms import AvailabilityForm
from roomBooking.booking_function.availabilty import check_availability

class RoomList(ListView):
    model=Room

class BookingList(ListView):
    model=RoomBooking

class BookingView(FormView):
    form_class= AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        available_rooms=[]
        for room in Room.objects.all():
            if  check_availability(room, data['start_datetime'], data['end_datetime']):
                available_rooms.append(room)
        if len(available_rooms)>0:
            room = available_rooms[0]
            booking = RoomBooking.objects.create(
                user = self.request.user,  
                room =room,
                start_datetime = data['start_datetime'],
                end_datetime = data['end_datetime']
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse("all rooms booked")
