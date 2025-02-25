from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import Room, RoomBooking
from .forms import AvailabilityForm
from booking_function.availabilty import check_availability

class RoomList(ListView):
    model=Room

class BookingList(ListView):
    model=RoomBooking

class BookingView(FormView):
    form_class= AvailabilityForm
    template_name = 'availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data