from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

from flightApp.authentication import CustomAuthToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('flightApp.urls')),
    # path('api-token-auth/', views.obtain_auth_token),
    path('api-token-auth/', CustomAuthToken.as_view())


]
