from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo.views import TodoView
from barb import views

router = routers.DefaultRouter()
router.register(r'todos', TodoView, 'todo')
router.register(r'barb/client', views.ClientView, 'client')
router.register(r'barb/services', views.ServicesView, 'services')
router.register(r'barb/barbers', views.BarberView, 'barbers')
router.register(r'barb/scheduling', views.SchedulingView, 'schedulings')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
