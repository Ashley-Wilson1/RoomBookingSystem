from django.contrib import admin
from .models import Room
from .models import RoomBooking
from .models import CustomUser
# adds information to /admin
admin.site.register(Room)
admin.site.register(RoomBooking)
admin.site.register(CustomUser)