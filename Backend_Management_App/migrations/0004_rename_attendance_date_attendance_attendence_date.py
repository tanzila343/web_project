# Generated by Django 3.2.5 on 2023-01-30 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend_Management_App', '0003_attendancereport_attendence'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='attendance_date',
            new_name='attendence_date',
        ),
    ]