from rest_framework import serializers
from .models import Flight, Booking

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'flight_number', 'date_and_time', 'total_seats']
        read_only_fields = ['id']  # id and views will be read-only fields

    def create(self, validated_data):
        return Flight.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.flight_number = validated_data.get('flight_number', instance.flight_number)
        instance.date_and_time = validated_data.get('date_and_time', instance.date_and_time)
        instance.total_seats = validated_data.get('total_seats', instance.total_seats)
        instance.save()
        return instance

class BookingSerializer(serializers.ModelSerializer):
    flight_number = serializers.StringRelatedField(source='flight.flight_number')
    username = serializers.StringRelatedField(source='user.username')
    class Meta:
        model = Booking
        fields = ['id', 'flight_number', 'username', 'seat_number', 'date_created']