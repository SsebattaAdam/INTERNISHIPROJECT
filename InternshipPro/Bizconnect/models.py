from django.db import models

# Create your models here.
from django.db import models

class Registration(models.Model):
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')))
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    district = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    country = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20, default='entrepreneur')
    role_in_company = models.CharField(max_length=100, choices=(('founder', 'Founder'), ('owner', 'Owner'), ('director', 'Director')))

    def __str__(self):
        return f"{self.firstname} {self.surname}"


from django.db import models
from django.contrib.postgres.fields import JSONField

class ExpertRegistration(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    DISTRICT_CHOICES = [
        ('bundibugyo', 'Bundibugyo'),
        ('gulu', 'Gulu'),
        ('jinja', 'Jinja'),
        ('kabarole', 'Kabarole'),
        ('kampala', 'Kampala'),
        ('lira', 'Lira'),
        ('masaka', 'Masaka'),
        ('mpigi', 'Mpigi'),
        ('mukono', 'Mukono'),
        ('soroti', 'Soroti'),
        ('wakiso', 'Wakiso'),
    ]

    COUNTRY_CHOICES = [
        ('uganda', 'Uganda'),
        ('tanzania', 'Tanzania'),
        ('kenya', 'Kenya'),
    ]

    surname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    district = models.CharField(max_length=20, choices=DISTRICT_CHOICES)
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    knowledge = models.JSONField()
    experience = models.JSONField()
    achievements = models.TextField()
    references = models.TextField()
    user_type = models.CharField(max_length=20, default='expert')

    def __str__(self):
        return f"{self.firstname} {self.surname}"


from django.db import models

class ServiceRequest(models.Model):
    business_idea = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    description = models.TextField()
    target_market = models.TextField()
    consultation_time = models.TimeField()
    consultation_date = models.DateField()
    urgency_level = models.CharField(max_length=10)
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_idea


