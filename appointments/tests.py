import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import Appointment


class AppointmentModelTests(TestCase):

    def test_is_upcoming_appointment(self):
        """
        is_upcoming() returns True for appointment whose app_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=10)
        appointment = Appointment(app_date = time)
        self.assertIs(appointment.is_upcoming(), True)

    def test_is_upcoming_old_appointment(self):
        """
        is_upcoming() returns False for appointment whose app_date
        is older than today.
        """
        time = timezone.now() - datetime.timedelta(days=2, minutes=20)
        appointment = Appointment(app_date = time)
        self.assertIs(appointment.is_upcoming(), False)


def create_appointment(description, days):
    """
    Create a appointment with the given `description` 
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Appointment.objects.create(description=description, 
                                      app_date=time)

class AppointmentIndexViewTests(TestCase):

    def test_no_appointments(self):
        response = self.client.get(reverse('appointments:app_index'))
        self.assertEqual(response.status_code, 200)
        self.assertIs(response.context['hide_form'], True)
        # self.assertQuerysetEqual(response.context['hide_form'], [])

    def test_getAppointments(self):
        create_appointment(description="Team meeting.", days=-30)
        response = self.client.post(reverse('appointments:app_list'), 
                                    {'keyword' : 'EE'})
        print(response.content)
        # print(len(response.content["list"]))
        # self.assertEqual(
        #     response.content['list'].size(), 1
        # )
        self.assertEqual(response.status_code, 200)





