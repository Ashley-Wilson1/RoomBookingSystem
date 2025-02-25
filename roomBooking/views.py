from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import Room, RoomBooking
from .forms import AvailabilityForm
from roomBooking.booking_function.availabilty import check_availability

class RoomList(ListView):
    model=Room

class BookingList(ListView):
    model=RoomBooking
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff: #super user also staff
            booking_list= RoomBooking.objects.all()
            return booking_list
        else:
            booking_list = RoomBooking.objects.filter(user=self.request.user) # only returns users bookings
            return booking_list

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_number = data['room_number']
        requested_room = Room.objects.get(number=room_number)  # Get the room based on the user selection

        # Check if the requested room is available
        if check_availability(requested_room, data['start_datetime'], data['end_datetime']):
            room = requested_room
        elif data['want_another_room']:
            # User wants another room, find the first available room
            available_rooms = [
                room for room in Room.objects.all()
                if check_availability(room, data['start_datetime'], data['end_datetime'])
            ]

            if available_rooms:
                room = available_rooms[0]  # Pick the first available room
            else:
                return HttpResponse("No rooms available for the selected time.", status=400)  # No rooms available
        else:
            return HttpResponse("Requested room is unavailable and user doesn't want another room.", status=400)

        # Create the booking with the selected room
        booking = RoomBooking.objects.create(
            user=self.request.user,
            room=room,
            start_datetime=data['start_datetime'],
            end_datetime=data['end_datetime']
        )
        return HttpResponse(f"Booking confirmed: Room {room.number} from {data['start_datetime']} to {data['end_datetime']}")