from django import forms
from .models import *
from django.contrib.auth import models, forms as auth_form
from phonenumber_field.formfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class AdminForm(auth_form.UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class DoctorSignUpForm(auth_form.UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class DoctorForm(forms.ModelForm):
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}),
                                    label=_("Phone number"), required=False)

    class Meta:
        model = DoctorModel
        exclude = ['user', 'status', ]


class AdminUpdateDoctor(forms.ModelForm):
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}),
                                    label=_("Phone number"), required=False)

    class Meta:
        model = DoctorModel
        fields = ['phone_number', 'address', 'profile_picture', 'visiting_charge', ]


class PatientSignUpForm(auth_form.UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class PatientForm(forms.ModelForm):
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}),
                                    label=_("Phone number"), required=False)

    class Meta:
        model = PatientModel
        exclude = ['user', 'status', ]


class PatientUpdateForm(forms.ModelForm):
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}),
                                    label=_("Phone number"), required=False)

    class Meta:
        model = PatientModel
        fields = ['phone_number', 'age', 'address', 'profile_pic']


class ReceptionistSignUpForm(auth_form.UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ReceptionistForm(forms.ModelForm):
    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}),
                                    label=_("Phone number"), required=False)

    class Meta:
        model = ReceptionistModel
        exclude = ['user', ]
