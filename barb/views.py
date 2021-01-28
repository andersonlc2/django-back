from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer, ServiceSerializer, BarberSerializer, SchedulingSerializer
from .models import Client, Services, Barber, Scheduling


class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()


class ServicesView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Services.objects.all()


class BarberView(viewsets.ModelViewSet):
    serializer_class = BarberSerializer
    queryset = Barber.objects.all()


class SchedulingView(viewsets.ModelViewSet):
    serializer_class = SchedulingSerializer
    queryset = Scheduling.objects.all()

