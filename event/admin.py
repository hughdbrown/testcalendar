from django.contrib import admin
from testcalendar.event.models import Event

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Event, EventAdmin)
