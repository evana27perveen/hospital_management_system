# Generated by Django 3.2 on 2021-04-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0007_auto_20210422_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admissionmodel',
            name='patient',
            field=models.CharField(max_length=50),
        ),
    ]
