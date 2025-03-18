# roomBooking/apps.py
from django.apps import AppConfig

class RoomBookingConfig(AppConfig):
    name = 'roomBooking'

    def ready(self):
        import roomBooking.signals  # Import the signals to ensure they are registered
