# Generated by Django 5.0.6 on 2024-08-10 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0009_alter_appointment_date_alter_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 10, 20, 53, 21, 887622)),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 10, 20, 53, 21, 887622)),
        ),
    ]
