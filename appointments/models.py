from django.utils import timezone
from django.db import models


class Appointment(models.Model):
    app_date = models.DateTimeField('Appointment date', null=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

    def is_upcoming(self):
        return self.app_date >= timezone.now()