from django.urls import path
from App_main import views

app_name = 'App_main'

urlpatterns = [
    # -------------Homes-------------#
    path('admin-home/', views.admin_home, name='AdminHome'),
    path('doctor-home/', views.doctor_home, name='DoctorHome'),
    path('receptionist-home/', views.receptionist_home, name='ReceptionistHome'),
    path('patient-home/', views.patient_home, name='PatientHome'),
    # -------------admin-------------#
    path('admin-doctor-view/', views.admin_doctor_view, name='AdminDoctorView'),
    path('admin-doctor-info/', views.admin_doctor_view_info, name='AdminDoctorViewInfo'),
    path('admin-add-new-doctor/', views.admin_doctor_view_add_doctor, name='AdminDoctorViewAddNewDoctor'),
    path('admin-doctor-update/<int:id>/', views.admin_updating_doctor_info, name='AdminDoctorUpdate'),
    path('admin-approve-doctor/', views.admin_approve_doctor, name='AdminApproveDoctor'),
    path('admin-doctor-approve-success/<int:pk>/', views.admin_approve_doctor_success,
         name='AdminApproveDoctorSuccess'),
    path('admin-doctor-approve-reject/<int:pk>/', views.admin_reject_doctor_success, name='AdminApproveDoctorReject'),
    path('admin-specialist-doctor-view/', views.admin_specialist_doctor_view, name='AdminSpecialistDoctorView'),
    path('admin-patient-view/', views.admin_patient_view, name='AdminPatientView'),
    path('admin-patient-info/', views.admin_patient_info, name='AdminPatientInfo'),
    path('admin-admitted-patient/', views.admin_admitted_patient, name='AdminAdmittedPatient'),
    path('admin-discharge-patient/', views.admin_discharge_patient, name='AdminDischargePatient'),
    path('admin-receptionist-view', views.admin_receptionist_view, name='AdminReceptionistView'),
    # -------------doctor-------------#
    path('doctor-profile-view/', views.doctor_profile_view, name='DoctorProfileView'),
    path('doctor-patient-view/', views.doctor_patient_view, name='DoctorPatientView'),
    path('doctor-my-patients/', views.doctor_my_patients, name='DoctorMyPatients'),
    path('doctor-discharged-patients', views.doctor_discharged_patients, name='DoctorDischargedPatients'),
    path('doctor-appointment-view/', views.doctor_appointment_view, name='DoctorAppointmentView'),
    # -------------receptionist-------------#
    path('receptionist-profile-view/', views.receptionist_profile_view, name='ReceptionistProfileView'),
    path('receptionist-doctor-view/', views.receptionist_doctor_view, name='ReceptionistDoctorView'),
    path('receptionist-admitted-patient/', views.receptionist_admitted_patient, name='ReceptionistAdmittedPatient'),
    path('receptionist-all-appointments/', views.receptionist_all_appointments, name='ReceptionistAllAppointments'),
    path('receptionist-discharged-patients/', views.receptionist_discharged_patients,
         name='ReceptionistDischargedPatients'),
    path('receptionist-give-appointment/', views.receptionist_give_appointment, name='ReceptionistGiveAppointment'),
    path('receptionist-admit-patient/', views.receptionist_admit_patient, name='ReceptionistAdmitPatient'),
    path('receptionist-discharge-patient/<int:pk>', views.receptionist_discharge_patient, name='ReceptionistDischargePatient'),
    path('receptionist-download-bill/<int:pk>/', views.receptionist_download_bill, name='ReceptionistDownloadBill'),
    # -------------Patient-------------#
    path('patient-applying-for-appointment/', views.patient_taking_appointment, name='PatientTakingAppointment'),
    path('patient-appointments/', views.patient_appointments, name='PatientAppointments'),
    path('patient-finds-doctors/', views.patient_finds_doctors, name='PatientFindsDoctors'),
    path('patient-update-profile/', views.patient_update_profile, name='PatientUpdateProfile'),
    path('receptionist-approve-appointments/', views.receptionist_approve_appointments,
         name='ReceptionistApproveAppointments'),
    path('receptionist-approve-appointment/<int:pk>/', views.receptionist_approve_appointment,
         name='ReceptionistApproveAppointment'),
    path('receptionist-reject-appointment/<int:pk>/', views.receptionist_reject_appointment,
         name='ReceptionistRejectAppointment'),

]
