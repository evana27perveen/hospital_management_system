import pdfkit
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import date

from App_main.forms import *
from App_login.models import *
from App_main.models import *
from App_login.forms import *


# Create your views here.
# User Group Finding
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()


def is_receptionist(user):
    return user.groups.filter(name='RECEPTIONIST').exists()


def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


# ------------- ADMIN ------------------#
@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_home(request):
    doctors = DoctorModel.objects.all()
    patients = AdmissionModel.objects.all()
    appointments = AppointmentModel.objects.all()
    dr_count = doctors.filter(status=True).count()
    dr_to_approve_count = doctors.filter(status=False).count()
    patient_count = patients.count()
    appointment_count = appointments.filter(status=True).count()
    appointment_to_approve_count = appointments.filter(status=False).count()
    context = {'doctors': doctors, 'patients': patients, 'appointments': appointments,
               'dr_count': dr_count, 'dr_to_approve_count': dr_to_approve_count, 'patient_count': patient_count,
               'appointment_count': appointment_count, 'appointment_to_approve_count': appointment_to_approve_count,
               }
    return render(request, 'App_main/Admin/admin_home.html', context=context)


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_doctor_view(request):
    return render(request, 'App_main/Admin/Admin_doctor_view.html')


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_doctor_view_info(request):
    doctors_info = DoctorModel.objects.filter(status=True)
    context = {'doctors_info': doctors_info}
    return render(request, 'App_main/Admin/admin_view_doctor_info.html', context=context)


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_doctor_view_add_doctor(request):
    form1 = DoctorSignUpForm()
    form2 = DoctorForm()
    if request.method == 'POST':
        form1 = DoctorSignUpForm(data=request.POST)
        form2 = DoctorForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            this_user = form1.save()
            doctor = form2.save(commit=False)
            doctor.user, doctor.status = this_user, True
            add_to_doctor_group = Group.objects.get_or_create('DOCTOR')
            add_to_doctor_group[0].user_set.add(this_user)
            return HttpResponseRedirect(reverse('App_main:AdminDoctorView'))
    context = {'form1': form1, 'form2': form2}
    return render(request, 'App_main/Admin/admin_doctor_view_add_doctor.html', context=context)


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_updating_doctor_info(request, id):
    user = DoctorModel.objects.get(id=id)
    form = AdminUpdateDoctor(instance=user)
    if request.method == 'POST':
        form = AdminUpdateDoctor(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_main:AdminDoctorViewInfo'))
    return render(request, 'App_main/Admin/admin_update_doctor.html', context={'form': form})


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_approve_doctor(request):
    doctor = DoctorModel.objects.filter(status=False)
    return render(request, "App_main/Admin/admin_approve_doctor_list.html", context={'doctor': doctor})


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_approve_doctor_success(request, pk):
    doctor = DoctorModel.objects.get(id=pk)
    doctor.status = True
    doctor.save()
    return HttpResponseRedirect(reverse('App_main:AdminApproveDoctor'))


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_reject_doctor_success(request, pk):
    doctor = DoctorModel.objects.get(id=pk)
    doctor.delete()
    return HttpResponseRedirect(reverse('App_main:AdminApproveDoctor'))


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_specialist_doctor_view(request):
    doctor = DoctorModel.objects.filter(status=True)
    # print(doctor[0].department)
    doctor_by_department = []
    for i in doctor:
        if i.department != 'MBBS':
            doctor_by_department.append(i)
    context = {'doctor_by_department': doctor_by_department}
    return render(request, 'App_main/Admin/admin_specialist_doctor_view.html', context=context)


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_patient_view(request):
    return render(request, 'App_main/Admin/admin_patient_view.html')


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_patient_info(request):
    patients = PatientModel.objects.all()
    context = {'patients': patients}
    return render(request, 'App_main/Admin/admin_patient_info.html', context=context)


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_admitted_patient(request):
    patients = AdmissionModel.objects.all()
    context = {'patients': patients}
    return render(request, 'App_main/Admin/admin_admitted_patient.html', context=context)


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_discharge_patient(request):
    discharged_patient = DischargeModel.objects.all()
    context = {'discharged_patient': discharged_patient}
    return render(request, 'App_main/Admin/admin_discharge_patient.html', context=context)


@login_required(login_url='App_login:AdminLogin')
@user_passes_test(is_admin)
def admin_receptionist_view(request):
    receptionist = ReceptionistModel.objects.all()
    context = {'receptionist': receptionist}
    return render(request, 'App_main/Admin/admin_receptionist_view.html', context=context)


# --------------------- DOCTOR ------------------#


@login_required(login_url='App_login:DoctorLogin')
@user_passes_test(is_doctor)
def doctor_home(request):
    my_patients = AdmissionModel.objects.filter(doctor__user=request.user)
    my_appointments = AppointmentModel.objects.filter(doctor__user=request.user)
    patient_count = my_patients.count()
    appointment_count = my_appointments.count()
    context = {'my_patients': my_patients, 'my_appointments': my_appointments, 'patient_count': patient_count,
               'appointment_count': appointment_count}
    return render(request, 'App_main/Doctor/doctor_home.html', context=context)


@login_required(login_url='App_login:DoctorLogin')
@user_passes_test(is_doctor)
def doctor_profile_view(request):
    doctor_profile = DoctorModel.objects.get(user=request.user)
    context = {'doctor_profile': doctor_profile}
    return render(request, 'App_main/Doctor/doctor_profile_view.html', context=context)


@login_required(login_url='App_login:DoctorLogin')
@user_passes_test(is_doctor)
def doctor_patient_view(request):
    # print(request.user.id)
    # print(AdmissionModel.objects.all()[0].doctor)
    my_patients_count = AdmissionModel.objects.filter(doctor=request.user.id).count()
    my_discharged_patients_count = DischargeModel.objects.filter(assigned_Doctor=request.user.id).count()
    context = {'my_patients_count': my_patients_count, 'my_discharged_patients_count': my_discharged_patients_count, }
    return render(request, 'App_main/Doctor/doctor_patient_view.html', context=context)


@login_required(login_url='App_login:DoctorLogin')
@user_passes_test(is_doctor)
def doctor_my_patients(request):
    my_patients = AdmissionModel.objects.filter(doctor=request.user.id)
    context = {'my_patients': my_patients}
    return render(request, 'App_main/Doctor/doctor_my_patients.html', context=context)


@login_required(login_url='App_login:DoctorLogin')
@user_passes_test(is_doctor)
def doctor_discharged_patients(request):
    discharged_patients = DischargeModel.objects.filter(assigned_Doctor=request.user.id)
    context = {'discharged_patients': discharged_patients}
    return render(request, 'App_main/Doctor/doctor_discharged_patients.html', context=context)


@login_required(login_url='App_login:DoctorLogin')
@user_passes_test(is_doctor)
def doctor_appointment_view(request):
    my_appointments = AppointmentModel.objects.filter(doctor=request.user.id)
    today = date.today()
    appointment_today = AppointmentModel.objects.filter(appointment_date=today)
    context = {'my_appointments': my_appointments, 'appointment_today': appointment_today}
    return render(request, 'App_main/Doctor/doctor_appointment_view.html', context=context)


# --------------------- Receptionist ------------------#


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_home(request):
    form = ReceptionistSideAppointmentForm()
    if request.method == 'POST':
        form = ReceptionistSideAppointmentForm(data=request.POST)
        if form.is_valid():
            my_form = form.save()
            messages.info(request, f"Appointment {my_form.cleaned_data.get('serial_number')} is confirmed")
            return HttpResponseRedirect(reverse('App_main:ReceptionistHome'))
    doctor_count = DoctorModel.objects.filter(status=True).count()
    doctor_to_approve = DoctorModel.objects.filter(status=False).count()
    appointment_count = AppointmentModel.objects.filter(status=True).count()
    appointment_to_approve_count = AppointmentModel.objects.filter(status=False).count()
    patient_count = AdmissionModel.objects.all().count()
    context = {'form': form, 'appointment_count': appointment_count, 'doctor_count': doctor_count,
               'appointment_to_approve_count': appointment_to_approve_count, 'patient_count': patient_count,
               'doctor_to_approve': doctor_to_approve}
    return render(request, 'App_main/Receptionist/receptionist_home.html', context=context)


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_profile_view(request):
    my_profile = ReceptionistModel.objects.get(user=request.user)
    context = {'my_profile': my_profile}
    return render(request, 'App_main/Receptionist/receptionist_profile_view.html', context=context)


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_doctor_view(request):
    doctors = DoctorModel.objects.filter(status=True)
    context = {'doctors': doctors}
    return render(request, 'App_main/Receptionist/receptionist_doctor_view.html', context=context)


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_all_appointments(request):
    appointments = AppointmentModel.objects.filter(status=True)
    context = {'appointments': appointments}
    return render(request, 'App_main/Receptionist/receptionist_all_appointments.html', context=context)


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_admitted_patient(request):
    patients = AdmissionModel.objects.all()
    context = {'patients': patients}
    return render(request, 'App_main/Receptionist/receptionist_admitted_patient.html', context=context)


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_discharged_patients(request):
    discharged_patients = DischargeModel.objects.all()
    context = {'discharged_patients': discharged_patients}
    return render(request, 'App_main/Receptionist/receptionist_discharged_patients.html', context=context)


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_give_appointment(request):
    form = ReceptionistSideAppointmentForm()
    if request.method == 'POST':
        form = ReceptionistSideAppointmentForm(data=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_main:ReceptionistHome'))
    context = {'form': form}
    return render(request, 'App_main/Receptionist/receptionist_give_appointment.html', context=context)


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_admit_patient(request):
    form = AdmissionForm()
    if request.method == 'POST':
        form = AdmissionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_main:ReceptionistHome'))
    context = {'form': form}
    return render(request, 'App_main/Receptionist/receptionist_admit_patient.html', context=context)


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_discharge_patient(request, pk):
    user = AdmissionModel.objects.get(id=pk)
    print(date.today())
    if TestModel.objects.filter(patient=user):
        test_cost = TestModel.objects.filter(patient=user)[0].testing_cost_in_total
    else:
        test_cost = 0
    form = DischargeForm()
    if request.method == 'POST':
        form = DischargeForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.patient = user.patient
            my_form.assigned_Doctor = user.doctor
            my_form.admitDate = user.admission_date
            my_form.symptoms = user.symptoms
            my_form.TestCharge = test_cost
            medical_cost = int(request.POST.get('medicineCost'))
            room_cost = int(request.POST.get('roomCharge'))
            doc_cost = int(request.POST.get('doctorFee'))
            other_cost = int(request.POST.get('OtherCharge'))
            total = medical_cost + room_cost + doc_cost + other_cost + int(test_cost)
            my_form.total = total
            my_form.save()
            user.delete()
            return HttpResponseRedirect(reverse('App_main:ReceptionistDischargedPatient'))
    context = {'form': form}
    return render(request, 'App_main/Receptionist/receptionist_discharge_patient.html', context=context)


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_download_bill(request, pk):
    discharged_user = DischargeModel.objects.get(id=pk)
    discharged_user.paid = True
    discharged_user.save()
    admit = discharged_user.admitDate
    release = discharged_user.releaseDate
    spent = (release-admit).days
    context = {'discharged_user': discharged_user, 'spent': spent}
    return render(request, 'App_main/Receptionist/receptionist_download_bill.html', context=context)


@login_required(login_url='App_login:ReceptionistLogin')
@user_passes_test(is_receptionist)
def receptionist_approve_appointments(request):
    appointment = AppointmentModel.objects.filter(status=False)
    context = {'appointment': appointment}
    return render(request, "App_main/Receptionist/receptionist_approve_appointments.html",
                  context=context)


def receptionist_approve_appointment(request, pk):
    user = AppointmentModel.objects.get(id=pk)
    form = ReceptionistApproveAppointmentForm(instance=user)
    if request.method == 'POST':
        form = ReceptionistApproveAppointmentForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_main:ReceptionistApproveAppointments'))
    context = {'form': form}
    return render(request, 'App_main/Receptionist/receptionist_approve_appointment.html', context=context)


def receptionist_reject_appointment(request, pk):
    appointment = AppointmentModel.objects.get(id=pk)
    appointment.delete()
    return HttpResponseRedirect(reverse('App_main:ReceptionistApproveAppointments'))


# --------------------- Patient ------------------#


@login_required(login_url='App_login:PatientLogin')
@user_passes_test(is_patient)
def patient_home(request):
    patient = PatientModel.objects.get(user=request.user)
    context = {'patient': patient}
    return render(request, 'App_main/Patient/patient_home.html', context=context)


@login_required(login_url='App_login:PatientLogin')
@user_passes_test(is_patient)
def patient_taking_appointment(request):
    form = PatientSideAppointmentForm()
    if request.method == 'POST':
        form = PatientSideAppointmentForm(data=request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            user = PatientModel.objects.get(user_id=request.user.id)
            my_form.patient = user
            my_form.save()
            return HttpResponseRedirect(reverse('App_main:PatientHome'))
    context = {'form': form}
    return render(request, 'App_main/Patient/patient_taking_appointment.html', context=context)


@login_required(login_url='App_login:PatientLogin')
@user_passes_test(is_patient)
def patient_appointments(request):
    appointments = AppointmentModel.objects.filter(patient__user=request.user)
    context = {'appointments': appointments}
    return render(request, 'App_main/Patient/patient_appointments.html', context=context)


@login_required(login_url='App_login:PatientLogin')
@user_passes_test(is_patient)
def patient_finds_doctors(request):
    doctors = DoctorModel.objects.filter(status=True)
    context = {'doctors': doctors}
    return render(request, 'App_main/Patient/patient_finds_doctors.html', context=context)


@login_required(login_url='App_login:PatientLogin')
@user_passes_test(is_patient)
def patient_update_profile(request):
    user = PatientModel.objects.get(user_id=request.user.id)
    form = PatientUpdateForm(instance=user)
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_main:PatientHome'))
    context = {'form': form}
    return render(request, 'App_main/Patient/patient_update_profile.html', context=context)
