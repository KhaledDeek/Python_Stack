# Generated by Django 5.1 on 2024-08-10 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0010_alter_appointment_date_alter_visit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 10, 23, 34, 1, 126548)),
        ),
        migrations.AlterField(
            model_name='visit',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 8, 10, 23, 34, 1, 126548)),
        ),
    ]
