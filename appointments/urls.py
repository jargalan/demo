from django.urls import path

from . import views

app_name = 'appointments'
urlpatterns = [
    path('', views.index, name='app_index'),
    path('add', views.add, name='app_add'),
    path('list', views.getAppointments, name='app_list'),
]