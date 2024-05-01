# Generated by Django 5.0.4 on 2024-04-30 23:46

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('phone_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator('^\\d{10,15}$')])),
                ('address', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('doctor_id', models.CharField(default='Doc_0000', max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{10,15}$')])),
                ('image', models.ImageField(blank=True, null=True, upload_to='doc-pics/')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='care_app.department')),
            ],
            options={
                'verbose_name_plural': 'Doctors',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('apppointment_id', models.CharField(default='A000', max_length=100, unique=True)),
                ('date', models.DateTimeField()),
                ('phone_number', models.CharField(max_length=15)),
                ('reason', models.TextField()),
                ('time', models.TimeField(default='00:00')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In_Progress', 'In Progress'), ('Completed', 'Completed')], default='Select', max_length=20)),
                ('department_of_appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='care_app.department')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='care_app.doctors')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='care_app.patients')),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
    ]
