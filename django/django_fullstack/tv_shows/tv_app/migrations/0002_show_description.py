# Generated by Django 5.0.6 on 2024-07-10 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(null=True),
        ),
    ]