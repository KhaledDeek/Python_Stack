# Generated by Django 5.0.6 on 2024-07-13 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0006_remove_course_comment_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='comments',
        ),
    ]