from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=25, blank=True, null=True)  
    last_name = models.CharField(max_length=25, blank=True, null=True)  
    email = models.EmailField(unique=True)  

    def __str__(self):
        return self.email  

class Room(models.Model):#maybe give int pk for custom rooms
    number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Room {self.number} (Capacity: {self.capacity})"

class RoomBooking(models.Model):
    
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.user.first_name} has booked Room {self.room.number} from {self.start_datetime} to {self.end_datetime}"


