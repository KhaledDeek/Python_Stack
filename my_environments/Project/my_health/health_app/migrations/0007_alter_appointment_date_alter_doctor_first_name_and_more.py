# Generated by Django 5.0.6 on 2024-08-10 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0006_alter_appointment_date_alter_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 10, 17, 46, 9, 978276)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(error_messages={'required': 'A contact needs a first name.'}, max_length=50),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 10, 17, 46, 9, 962652)),
        ),
    ]
