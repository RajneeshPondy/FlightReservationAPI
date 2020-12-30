from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    operating_airlines = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=30, blank=True)
    arrival_city = models.CharField(max_length=30)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()

    def __str__(self):
        return f"Flight No : {self.flight_number}"


class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservation(models.Model):
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name : {self.passenger.first_name} ,  Flight : {self.flight_number}"
