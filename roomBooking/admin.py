from django.contrib import admin
from .models import Room
from .models import RoomBooking
from .models import User
# adds information to /admin
admin.site.register(Room)
admin.site.register(RoomBooking)
