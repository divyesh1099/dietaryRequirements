from django.db import models
from django.utils import timezone

class DietaryPreference(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    diet = models.CharField(max_length=50)
    diseases = models.TextField(blank=True)  # Assuming multiple diseases can be entered
    allergies = models.TextField(blank=True)  # Assuming multiple allergies can be entered

    def __str__(self):
        return self.name
    
from django.db import models

class InvitationDetail(models.Model):
    party_title = models.CharField(max_length=200)
    party_message = models.TextField()
    party_date = models.DateField(default=timezone.now)
    party_time = models.CharField(max_length=50)
    party_location = models.CharField(max_length=200)
    optional_desserts = models.CharField(max_length=200)
    gift = models.BooleanField(default=False)
    gift_message = models.TextField()
    timezone = models.CharField(max_length=40)

    def __str__(self):
        return self.party_title

class DietPreference(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
