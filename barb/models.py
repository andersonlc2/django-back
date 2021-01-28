import datetime as dt
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Client(AbstractUser):
    tel = models.IntegerField(blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=120, blank=True)
    number = models.IntegerField(blank=True, null=True)
    complement = models.CharField(max_length=120, blank=True)
    district = models.CharField(max_length=120, blank=True)
    city = models.CharField(max_length=120, blank=True)
    state = models.CharField(max_length=120, blank=True)
    added = models.DateField(auto_now_add=True, editable=False, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def addres(self):
        addres_comp = {
            'zip_code': self.zip_code,
            'street': self.street,
            'number': self.number,
            'complement': self.complement,
            'district': self.district,
            'city': self.city,
            'state': self.state
        }
        return addres_comp


class Services(models.Model):
    hair = models.BooleanField(default=False)
    beard = models.BooleanField(default=False)
    sealing = models.BooleanField(default=False)


class Barber(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    tel = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Scheduling(models.Model):
    hour = models.DateTimeField("hour of scheduling")
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    serviceHair = models.BooleanField(default=False)
    serviceBeard = models.BooleanField(default=False)
    serviceSealing = models.BooleanField(default=False)

    def __str__(self):
        dif = dt.timedelta(hours=-3)
        tz = dt.timezone(dif)
        hour = self.hour.astimezone(tz)
        return f"Agendado para dia {hour.strftime('%d/%m/%Y as %H:%M h')}"

    def hour_finish(self):
        dif = dt.timedelta(hours=-3)
        tz = dt.timezone(dif)
        hour = self.hour.astimezone(tz)
        finish = hour
        if self.serviceHair:
            finish += dt.timedelta(minutes=30)
        if self.serviceBeard:
            finish += dt.timedelta(minutes=15)
        if self.serviceSealing:
            finish += dt.timedelta(minutes=45)
        return finish.strftime('%H:%M')