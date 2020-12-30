from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    operating_airlines = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=30)
    arrival_city = models.CharField(max_length=30)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()


class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)


class Reservation(models.Model):
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE)
