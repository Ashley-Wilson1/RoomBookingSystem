import _datetime
from roomBooking.models import Room, RoomBooking

def check_availability(room, start_datetime, end_datetime):
    avail_list = []
    booking_list = RoomBooking.objects.filter(room = room)
    for booking in booking_list:
        if booking.start_datetime > end_datetime or booking.end_datetime < start_datetime:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list) #returns true if all items are true. 