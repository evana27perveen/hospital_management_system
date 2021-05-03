from django import forms
from App_main.models import *


class PatientSideAppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentModel
        fields = ['doctor', 'symptoms', ]


class ReceptionistSideAppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentModel
        fields = '__all__'


class ReceptionistApproveAppointmentForm(forms.ModelForm):
    appointment_date = forms.CharField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = AppointmentModel
        fields = ['serial_number', 'appointment_date', 'status', ]


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionModel
        exclude = ['admission_date', ]


class TestForm(forms.ModelForm):
    class Meta:
        model = TestModel
        fields = '__all__'


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBackModel
        exclude = ['user', ]


class DischargeForm(forms.ModelForm):
    class Meta:
        model = DischargeModel
        exclude = ['total', 'admitDate', 'releaseDate', 'patient', 'assigned_Doctor', 'symptoms', 'TestCharge', 'paid', ]

