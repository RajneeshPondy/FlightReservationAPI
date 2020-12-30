from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
        FlightViewSet,
        PassengerViewSet,
        ReservationViewSet
)

router = DefaultRouter()
router.register('flight', FlightViewSet)
router.register('passernger', PassengerViewSet)
router.register('reservation', ReservationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    
]
