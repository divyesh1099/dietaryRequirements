from django.contrib import admin
from .models import *
# Register your models here.
class DietaryPreferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'diet', 'diseases', 'allergies')  # Customize the columns displayed
    list_filter = ('diet',)  # Enable filtering by diet
    search_fields = ('name', 'diseases', 'allergies')  # Enable search

admin.site.register(DietaryPreference, DietaryPreferenceAdmin)
admin.site.register(InvitationDetail)
admin.site.register(DietPreference)
