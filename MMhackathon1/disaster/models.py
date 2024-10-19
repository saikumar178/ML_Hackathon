# disaster/models.py

from django.db import models


class Disaster(models.Model):
    disaster_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_reported = models.DateField(auto_now_add=True)
    volunteer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.disaster_type} at {self.location}"

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    skills = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name