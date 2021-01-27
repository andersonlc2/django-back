import datetime as dt
from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    tel = models.IntegerField()
    date_birth = models.DateField("date of birth")
    zip_code = models.IntegerField()
    street = models.CharField(max_length=120)
    number = models.IntegerField()
    complement = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    
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
        return f"Agendado para {self.hour} "

    def hour_finish(self):
        finish = self.hour
        if self.serviceHair:
            finish += dt.timedelta(minutes=30)
        elif self.serviceBeard:
            finish += dt.timedelta(minutes=15)
        elif self.serviceSealing:
            finish += dt.timedelta(minutes=45)
        return finish
