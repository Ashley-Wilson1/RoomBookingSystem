from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=25, blank=True, null=True)  
    last_name = models.CharField(max_length=25, blank=True, null=True)  
    email = models.EmailField(unique=True)  

    def __str__(self):
        return self.email  

class Room(models.Model):
    capacity = models.IntegerField()

    def __str__(self):
        return f"Room {self.id} (Capacity: {self.capacity})"

class RoomBooking(models.Model):
    name = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)  # Allow nulls to avoid migration issues

    def __str__(self):
        return f"{self.name} by {self.user.username}"


