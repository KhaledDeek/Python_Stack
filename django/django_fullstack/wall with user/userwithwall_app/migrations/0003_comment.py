# Generated by Django 5.0.6 on 2024-07-18 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userwithwall_app', '0002_alter_user_email_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('messages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='userwithwall_app.message')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='userwithwall_app.user')),
            ],
        ),
    ]