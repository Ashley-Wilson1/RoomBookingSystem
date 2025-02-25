from django import forms
from .models import Room

class AvailabilityForm(forms.Form):  # Fix typo (was AvailabiltyForm)
    room_number = forms.ChoiceField(choices=[],required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room_number'].choices = [(room.number, room.number) for room in Room.objects.all()]

    start_datetime = forms.DateTimeField(required=True,input_formats=["%y-%m-%dT%H:%M",])
    end_datetime = forms.DateTimeField(required=True,input_formats=["%y-%m-%dT%H:%M",])

