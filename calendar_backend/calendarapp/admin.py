from calendarapp.models import Event,Reminder
from django.contrib import admin
from .models import Event, Reminder


# Register your models here.
from .models import Event, Reminder

admin.site.register(Event)
admin.site.register(Reminder)

