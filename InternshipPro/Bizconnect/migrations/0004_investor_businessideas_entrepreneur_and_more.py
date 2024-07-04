# Generated by Django 5.0.6 on 2024-07-04 11:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bizconnect', '0003_merge_20240704_1440'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('individual', 'Individual'), ('organization', 'Organization')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=50)),
                ('capital', models.CharField(max_length=100)),
                ('information', models.TextField()),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('tourism', models.BooleanField(default=False)),
                ('media', models.BooleanField(default=False)),
                ('commercial', models.BooleanField(default=False)),
                ('estate', models.BooleanField(default=False)),
                ('manufacturing', models.BooleanField(default=False)),
                ('education', models.BooleanField(default=False)),
                ('health', models.BooleanField(default=False)),
                ('wholesale', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='businessideas',
            name='entrepreneur',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='business_ideas', to='Bizconnect.registration'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expertregistration',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registration',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='requester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Bizconnect.registration'),
        ),
        migrations.CreateModel(
            name='ConsultationPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('package_type', models.CharField(choices=[('hourly', 'Hourly Rate'), ('retainer', 'Retainer-based'), ('project', 'Project-Based'), ('specialised', 'Specialised Challenge'), ('growth', 'Growth Strategy')], max_length=20)),
                ('package_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bizconnect.expertregistration')),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentDeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('funding_goal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valuation', models.DecimalField(decimal_places=2, max_digits=10)),
                ('terms', models.TextField()),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bizconnect.registration')),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentFunds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('industry', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('equity', 'Equity'), ('debt', 'Debt'), ('convertible_note', 'Convertible Note')], max_length=100)),
                ('investment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact_method', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone')], max_length=100)),
                ('notes', models.TextField()),
                ('supporting_documents', models.FileField(blank=True, null=True, upload_to='supporting_documents/')),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investment_fund', to='Bizconnect.registration')),
            ],
        ),
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
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=10)),
                ('denial_reason', models.TextField(blank=True, null=True)),
                ('consultation_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bizconnect.consultationpackage')),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_meeting', to='Bizconnect.registration')),
            ],
        ),
    ]
