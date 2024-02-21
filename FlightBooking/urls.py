"""
URL configuration for FlightBooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Flights.views import all_flights, filter_flights, book_flight, booked_flights
from Users.views import signup, login, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup),
    path('login/', login),
    path('logout/', logout_user),
    path('flights/', all_flights, name='all_flights'),
    path('flights/filter/', filter_flights, name='filter_flights'),   
    path('flights/booking/<str:flight_number>', book_flight, name='book_flight'),
    path('flights/booked/', booked_flights, name='booked_flights')
]
