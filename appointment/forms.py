from django import forms
from .models import Appointment, Prescription
from account.models import User


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = User.objects.filter(usertype='P')

        # self.fields['patient'].empty_label = 'select patient'
        self.fields['doctor'].queryset = User.objects.filter(usertype='D')

        # self.fields['doctor'].empty_label = 'select doctor'


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        exclude = ['doctor']
        widgets = {
            'prescription': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient'].queryset = User.objects.filter(usertype='P')
