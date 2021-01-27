from django.contrib import admin
from .models import Client, Services, Barber, Scheduling

# Clients
class ClientAdmin(admin.ModelAdmin):  # add this
    list_display = ('__str__', 'tel')


# Services
class ServicesAdmin(admin.ModelAdmin):  # add this
    list_display = ('hair', 'beard', 'sealing')


# Barbers
class BarberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tel')

# Schedulings
class SchedulingAdmin(admin.ModelAdmin):
    list_display = ('client', '__str__', 'barber')



# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Barber, BarberAdmin)
admin.site.register(Scheduling, SchedulingAdmin)
