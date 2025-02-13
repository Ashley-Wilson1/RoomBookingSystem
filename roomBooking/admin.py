from django.contrib import admin
from .models import Room
from .models import RoomBooking
from .models import User

admin.site.register(Room)
admin.site.register(RoomBooking)
admin.site.register(User)