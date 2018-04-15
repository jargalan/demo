import datetime

from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(help_text="MM/DD/YYYY")
    time = forms.TimeField(help_text="HH:MM")

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['time'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-sm'

    def save(self, commit=True):
        instance = super(AppointmentForm, self).save(commit=False)
        
        if commit:
            if self.cleaned_data.get('date') and self.cleaned_data.get('time'):
                instance.app_date = \
                    datetime.datetime.combine(self.cleaned_data.get('date'), 
                                              self.cleaned_data.get('time'))
            instance.save()
        return instance

    class Meta:
        model = Appointment
        fields = ['date', 'time', 'description']
        help_texts = {
            'description': 'Appointment description',
        }