from rest_framework import serializers
from .models import Client, Services, Barber, Scheduling


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            'first_name', 
            'last_name', 
            'email', 
            'tel',
            'date_birth',
            'addres',
        )


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = (
            'hair',
            'beard',
            'sealing',
        )


class BarberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barber
        fields = (
            'first_name',
            'last_name',
            'tel',
        )


class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        fields = (
            'hour',
            'barber',
            'client',
            'serviceHair',
            'serviceBeard',
            'serviceSealing',
            'hour_finish',
        )
