import datetime
from roomBooking.models import Room, RoomBooking



def check_availability(room, start_datetime, end_datetime):
    # Check if there is any overlapping booking
    overlapping_bookings = RoomBooking.objects.filter(
        room=room,
        start_datetime__lt=end_datetime,  # Existing booking starts before new booking ends
        end_datetime__gt=start_datetime   # Existing booking ends after new booking starts
    )
    return not overlapping_bookings.exists()  # Returns True if no overlapping bookings

# def check_availability(room, start_datetime, end_datetime):
#     avail_list = []
#     booking_list = RoomBooking.objects.filter(room = room)
#     for booking in booking_list:
#         if booking.start_datetime > end_datetime or booking.end_datetime < start_datetime:
#             avail_list.append(True)
#         else:
#             avail_list.append(False)
#     return all(avail_list) #returns true if all items are true. 