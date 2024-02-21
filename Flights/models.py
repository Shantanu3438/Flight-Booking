from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=50)
    date_and_time = models.DateTimeField()
    total_seats = models.IntegerField()
    available_seats = models.IntegerField(default=None)

    def __str__(self):
        return self.flight_number

    def save(self, *args, **kwargs):
        if self.available_seats is None:
            self.available_seats = self.total_seats
        super().save(*args, **kwargs)


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Booking #{self.id} - Flight {self.flight.flight_number}, Seat {self.seat_number}"
