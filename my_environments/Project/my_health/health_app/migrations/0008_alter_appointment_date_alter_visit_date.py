# Generated by Django 5.0.6 on 2024-08-10 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0007_alter_appointment_date_alter_doctor_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 10, 19, 8, 21, 287200)),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 10, 19, 8, 21, 287200)),
        ),
    ]
