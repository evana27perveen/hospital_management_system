# Generated by Django 3.2 on 2021-04-16 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceptionistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=50)),
                ('salary', models.PositiveIntegerField()),
                ('profile_picture', models.ImageField(upload_to='receptionist_pic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptionist_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(upload_to='patient_picture')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_uesr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=20)),
                ('reg_num', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(upload_to='doctor_profile_picture')),
                ('visiting_charge', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doc_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
