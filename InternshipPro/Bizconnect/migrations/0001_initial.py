# Generated by Django 5.0.6 on 2024-06-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('district', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=255)),
                ('role_in_company', models.CharField(choices=[('founder', 'Founder'), ('owner', 'Owner'), ('director', 'Director')], max_length=100)),
            ],
        ),
    ]