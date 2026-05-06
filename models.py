from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TouristProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class SOSAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"SOS from {self.user.username} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
