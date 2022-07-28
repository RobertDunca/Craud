from django.contrib import admin

from trip.models import Event, Restaurant, ThingToDo

admin.site.register(Event)
admin.site.register(Restaurant)
admin.site.register(ThingToDo)
