from django.db import models

class DietaryPreference(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    diet = models.CharField(max_length=50)
    diseases = models.TextField(blank=True)  # Assuming multiple diseases can be entered
    allergies = models.TextField(blank=True)  # Assuming multiple allergies can be entered

    def __str__(self):
        return self.name