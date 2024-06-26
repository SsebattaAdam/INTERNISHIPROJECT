# Generated by Django 5.0.6 on 2024-06-27 12:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bizconnect', '0005_expertregistration_user_consultationpackage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('expert_name', models.CharField(max_length=255)),
                ('consultation_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('link', models.URLField()),
                ('consultation_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bizconnect.consultationpackage')),
            ],
        ),
    ]
