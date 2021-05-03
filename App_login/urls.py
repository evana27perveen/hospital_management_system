from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


app_name = 'App_login'


urlpatterns = [
    path('admin-signup/', views.admin_signup, name='AdminSignup'),
    path('doctor-signup/', views.doctor_profile, name='DoctorSignup'),
    path('patient-signup/', views.patient_profile, name='PatientSignup'),
    path('receptionist-signup/', views.receptionist_profile, name='ReceptionistSignup'),
    path('admin-login/', views.admin_login, name='AdminLogin'),
    path('doctor-login/', views.doctor_login, name='DoctorLogin'),
    path('patient-login/', views.patient_login, name='PatientLogin'),
    path('receptionist-login/', views.receptionist_login, name='ReceptionistLogin'),
    path('logout/', views.logout_system, name='logout'),
]
