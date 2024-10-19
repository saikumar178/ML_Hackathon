# disaster/forms.py

from django import forms
from .models import Disaster

class DisasterForm(forms.ModelForm):
    class Meta:
        model = Disaster
        fields = ['disaster_type', 'location', 'volunteer_name']
# disaster/forms.py
from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['name', 'skills', 'location']
