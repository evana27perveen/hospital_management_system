# Generated by Django 3.2 on 2021-04-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0004_alter_appointmentmodel_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dischargemodel',
            name='TestChange',
        ),
        migrations.AddField(
            model_name='dischargemodel',
            name='TestCharge',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
