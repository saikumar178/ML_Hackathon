# disaster/admin.py

from django.contrib import admin
from .models import Disaster, Volunteer

admin.site.register(Disaster)
admin.site.register(Volunteer)
