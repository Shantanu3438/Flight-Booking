from django.contrib import admin

from .models import Flight

class FlightAdmin(admin.ModelAdmin):
    # Define which fields are displayed in the admin interface
    list_display = ('flight_number', 'date_and_time', 'total_seats')
    # Optionally, you can add filters or search functionality
    list_filter = ('date_and_time',)
    search_fields = ('flight_number',)

admin.site.register(Flight, FlightAdmin)