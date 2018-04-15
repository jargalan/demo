from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse

from .models import Appointment
from .forms import AppointmentForm


def index(request):
    form = AppointmentForm()

    context = {
        'form': form, 
        'hide_form': True
    }
    return render(request, 'appointments/index.html', context)


def getAppointments(request):
    keyword = request.POST.get('keyword', '').strip()
    select_data = {"app_date_format": """strftime('%%m/%%d/%%Y %%H:%%M:%%S', app_date)"""}

    appointment_list = Appointment.objects.extra(select=select_data).order_by('app_date')
    if len(keyword) > 0:
        appointment_list = appointment_list.filter(description__icontains=keyword)

    data = {
        'list': list(appointment_list.values("app_date_format", "description"))
    }
    return JsonResponse(data)


def add(request):
    form = AppointmentForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('appointments:app_index'))

    context = {
        'form': form, 
        'hide_form': False
    }
    return render(request, 'appointments/index.html', context)



