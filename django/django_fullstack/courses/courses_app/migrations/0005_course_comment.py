# Generated by Django 5.0.6 on 2024-07-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0004_remove_course_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
