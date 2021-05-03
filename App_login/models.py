from django.db import models
from django.contrib.auth.models import User, AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class DoctorModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doc_user')
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=50)
    department = models.CharField(max_length=20)
    reg_num = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='doctor_profile_picture')
    visiting_charge = models.PositiveIntegerField()
    status = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def department_return(self):
        return f"{self.department}"

    @property
    def visiting_amount(self):
        return f"{self.visiting_charge}"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class PatientModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_uesr')
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='patient_picture')

    def patient_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def contact(self):
        return f"{self.patient_name()} {self.phone_number}"

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class ReceptionistModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receptionist_user')
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()
    profile_picture = models.ImageField(upload_to='receptionist_pic')


