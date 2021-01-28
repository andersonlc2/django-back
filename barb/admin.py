from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import Client, Services, Barber, Scheduling


# Clients
@admin.register(Client)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Client
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (None, {'fields': ('tel',)}),
    )
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     (('Personal info'), {'fields': ('first_name', 'last_name', "tel", "date_birth",)}),
    #     ("Address", {"fields": ("zip_code", "street", "number", "complement",
    #         "district", "city", "state",)}),
    #     (('Permissions'), {
    #         'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
    #     }),
    #     (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    # )
    # add_fieldsets = (
    # (None, {'fields': ('email', 'password1', 'first_name', 'last_name', "tel", "date_birth",),
    # }),
    # ("Address", {"fields": ("zip_code", "street", "number", "complement", "district", "city", "state",),
    # }),
    # )
    # list_display = ('email', 'first_name', 'last_name', 'is_staff')


# Services
class ServicesAdmin(admin.ModelAdmin):  # add this
    list_display = ('hair', 'beard', 'sealing')


# Barbers
class BarberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tel')


# Schedulings
class SchedulingAdmin(admin.ModelAdmin):
    list_display = ('client', 'hour', 'hour_finish', 'barber')
    list_filter = ['hour']


# Register your models here.
admin.site.register(Services, ServicesAdmin)
admin.site.register(Barber, BarberAdmin)
admin.site.register(Scheduling, SchedulingAdmin)

