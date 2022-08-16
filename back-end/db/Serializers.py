from rest_framework import serializers
from .models import Airlines,Countries,Customers,Tickets,Flights
from django.contrib.auth.models import User



class AirlinesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Airlines
        fields ='__all__'

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model =Countries
        fields ='__all__'

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model =Customers
        fields ='__all__'

class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Tickets
        fields ='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields ='__all__'

class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Flights
        fields ='__all__'



