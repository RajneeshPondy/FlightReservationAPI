from django.db.models import Q

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields  = ['flight_number', 'departure_city']


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


@api_view(['POST'])
def find_flights(request):
    data = request.data
    filters_queries = (
        Q(flight_number=data["flight_number"]) |
        Q(departure_city=data["departure_city"]) |
        Q(date_of_departure=data["date_of_departure"])
    )

    flights = Flight.objects.filter(filters_queries)
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data["id"])

    passenger = Passenger()
    passenger.first_name = request.data["first_name"]
    passenger.middle_name = request.data["middle_name"]
    passenger.last_name = request.data["last_name"]
    passenger.email = request.data["email"]
    passenger.phone = request.data["phone"]
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)
