from django.db import models
from App_login.models import DoctorModel, PatientModel, ReceptionistModel
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

Room_Category = [
    ('Cabin', 'Cabin'),
    ('ward', 'ward'),
    ('twin share room', 'twin share room'),
    ('suite', 'suite'),
    ('ICU', 'ICU'),
]


# Create your models here.
# Appointment, Admission, Testing, Discharge, Feedback


class AppointmentModel(models.Model):
    doctor = models.ForeignKey(DoctorModel, on_delete=models.DO_NOTHING, related_name='appointment_doctor')
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE, related_name='appointment_patient')
    symptoms = models.TextField()
    appointment_date = models.DateTimeField(null=True, blank=True)
    serial_number = models.PositiveIntegerField(null=True, blank=True)
    status = models.BooleanField(default=False)


class AdmissionModel(models.Model):
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE, related_name='recommended_doctor')
    patient = models.CharField(max_length=50)
    room_type = models.CharField(choices=Room_Category, max_length=200)
    room_number = models.CharField(max_length=50)
    bed_number = models.CharField(max_length=20)
    admission_date = models.DateField(auto_now=True)
    symptoms = models.TextField()

    def patient_info(self):
        return f"{self.patient}-Room:{self.room_number} Bed:{self.bed_number}"

    def __str__(self):
        return f"{self.patient}-Room:{self.room_number} Bed:{self.bed_number}"


class TestModel(models.Model):
    patient = models.ForeignKey(AdmissionModel, on_delete=models.CASCADE, related_name='test_patient')
    test = models.TextField()
    testing_cost_in_total = models.PositiveIntegerField()

    def __str__(self):
        return f"Mr. {self.patient.patient} {self.patient.room_number} {self.patient.bed_number}, cost: {self.testing_cost_in_total}"


class FeedBackModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()


class DischargeModel(models.Model):
    patient = models.CharField(max_length=100, null=False)
    assigned_Doctor = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=40)
    mobile = PhoneNumberField()
    symptoms = models.CharField(max_length=100, null=True)
    admitDate = models.DateField(null=False)
    releaseDate = models.DateField(auto_now=True)
    roomCharge = models.PositiveIntegerField(null=False)
    medicineCost = models.PositiveIntegerField(null=False)
    doctorFee = models.PositiveIntegerField(null=False)
    OtherCharge = models.PositiveIntegerField(null=False)
    TestCharge = models.PositiveIntegerField(null=True)
    total = models.PositiveIntegerField(null=False)
    paid = models.BooleanField(default=False)
