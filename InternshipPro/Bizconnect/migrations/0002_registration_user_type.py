# Generated by Django 5.0.6 on 2024-06-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bizconnect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='user_type',
            field=models.CharField(default='entrepreneur', max_length=20),
        ),
    ]
