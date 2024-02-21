from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Flight, Booking
from rest_framework.permissions import IsAuthenticated
from .serializers import FlightSerializer, BookingSerializer
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_flight(request):
    serializer = FlightSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def remove_flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    flight.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def all_flights(request):
    flights = Flight.objects.all()
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def filter_flights(request):
    query = request.data.get('datetime')
    if query:
        flights = Flight.objects.filter(date_and_time__contains=query)
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)
    else:
        return Response({"message": "Please provide a date and time to filter flights."}, status=400)
    


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_flight(request, flight_number):
    if not flight_number:
        return Response({"message": "Flight ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        flight = Flight.objects.get(flight_number=flight_number)
    except Flight.DoesNotExist:
        return Response({"message": "Flight not found."}, status=status.HTTP_404_NOT_FOUND)

    # Check if the flight has available seats
    if flight.total_seats <= 0:
        return Response({"message": "No available seats for this flight."}, status=status.HTTP_400_BAD_REQUEST)

    # Allocate a seat number and create a booking
    seat_number = flight.total_seats - flight.total_seats + 1
    user = request.user  # Get the authenticated user
    booking = Booking.objects.create(flight=flight, seat_number=seat_number, user=user)

    # Update available seats count
    flight.total_seats -= 1
    flight.save()

    return Response({"message": "Booking successful.", "booking_id": booking.id, "seat_number": seat_number}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def booked_flights(request):
    bookings = Booking.objects.filter(user=request.user)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)