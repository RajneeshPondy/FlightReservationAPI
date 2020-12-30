from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
        FlightViewSet,
        PassengerViewSet,
        ReservationViewSet,
        find_flights,
        save_reservation
)

router = DefaultRouter()
router.register('flight', FlightViewSet)
router.register('passernger', PassengerViewSet)
router.register('reservation', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('find-flights/', find_flights, name='find-flight'),
    path('save-reservation/', save_reservation, name='save-reservation')    
]
