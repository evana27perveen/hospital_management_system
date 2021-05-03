from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import *
from .forms import *


# Create your views here.


def admin_signup(request):
    form = AdminForm()
    if request.method == 'POST':
        form = AdminForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            admin_grp = Group.objects.get_or_create(name='ADMIN')
            admin_grp[0].user_set.add(user)
            return HttpResponseRedirect(reverse('App_login:AdminLogin'))
    return render(request, 'App_login/signup.html', context={'form': form})


def doctor_profile(request):
    form1 = DoctorSignUpForm()
    form2 = DoctorForm()
    if request.method == 'POST':
        form1 = DoctorSignUpForm(data=request.POST)
        form2 = DoctorForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            my_form1 = form1.save()
            my_form2 = form2.save(commit=False)
            my_form2.user = my_form1
            my_form2.save()
            doctor_grp = Group.objects.get_or_create(name='DOCTOR')
            doctor_grp[0].user_set.add(my_form1)
            return HttpResponseRedirect(reverse('App_login:DoctorLogin'))
    return render(request, 'App_login/doctor_signup.html', context={'form1': form1, 'form2': form2})


def patient_profile(request):
    form1 = PatientSignUpForm()
    form2 = PatientForm()
    if request.method == 'POST':
        form1 = PatientSignUpForm(data=request.POST)
        form2 = PatientForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            my_form1 = form1.save()
            my_form2 = form2.save(commit=False)
            my_form2.user = my_form1
            my_form2.save()
            patient_group = Group.objects.get_or_create(name='PATIENT')
            patient_group[0].user_set.add(my_form1)
            return HttpResponseRedirect(reverse('App_login:PatientLogin'))
    return render(request, 'App_login/patient_signup.html', context={'form1': form1, 'form2': form2})


def receptionist_profile(request):
    form1 = ReceptionistSignUpForm()
    form2 = ReceptionistForm()
    if request.method == 'POST':
        form1 = ReceptionistSignUpForm(data=request.POST)
        form2 = ReceptionistForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            my_form1 = form1.save()
            my_form2 = form2.save(commit=False)
            my_form2.user = my_form1
            my_form2.save()
            receptionist_group = Group.objects.get_or_create(name='RECEPTIONIST')
            receptionist_group[0].user_set.add(my_form1)
            return HttpResponseRedirect(reverse('App_login:ReceptionistLogin'))
    return render(request, 'App_login/receptionist_signup.html', context={'form1': form1, 'form2': form2})


def admin_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_main:AdminHome'))
    return render(request, 'App_login/admin_login.html', context={'form': form})


def doctor_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_main:DoctorHome'))
    return render(request, 'App_login/doctor_login.html', context={'form': form})


def patient_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_main:PatientHome'))
    return render(request, 'App_login/patient_login.html', context={'form': form})


def receptionist_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_main:ReceptionistHome'))
    return render(request, 'App_login/receptionist_login.html', context={'form': form})


def logout_system(request):
    logout(request)
    return HttpResponseRedirect(reverse('AccountHome'))
