from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

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
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    assigned_expert = models.ForeignKey('ExpertRegistration', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_requests',)
    requester = models.ForeignKey(Registration, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.business_idea} by {self.requester.firstname} {self.requester.surname}"




class BusinessIdeas(models.Model):
    entrepreneur = models.ForeignKey(Registration, related_name='business_ideas', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    industry = models.CharField(max_length=100)
    target_market = models.TextField()
    business_model = models.TextField()
    projections = models.TextField()
    goals = models.TextField(blank=True, null=True)
    pitch_deck = models.FileField(upload_to='attachments/pitch_deck/', blank=True, null=True)
    plan = models.FileField(upload_to='attachments/plan/', blank=True, null=True)
    video = models.FileField(upload_to='attachments/video/', blank=True, null=True)
    support = models.FileField(upload_to='attachments/support/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class InvestmentDeal(models.Model):
    entrepreneur = models.ForeignKey(Registration, related_name='investment_deals', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    funding_goal = models.DecimalField(max_digits=10, decimal_places=2)
    valuation = models.DecimalField(max_digits=10, decimal_places=2)
    terms = models.TextField()

    def __str__(self):
        return self.title
    


class ConsultationPackage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    package_type = models.CharField(max_length=50, choices=[
        ('Hourly Rate', 'Hourly Rate'),
        ('Retainer-based', 'Retainer-based'),
        ('Project-Based', 'Project-Based'),
        ('Specialised Challenge', 'Specialised Challenge'),
        ('Growth Strategy', 'Growth Strategy'),
    ])
    package_price = models.DecimalField(max_digits=10, decimal_places=2)
    expert = models.ForeignKey(ExpertRegistration, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    



    

class ScheduledMeeting(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Denied', 'Denied')
    ]
    entrepreneur = models.ForeignKey(Registration, related_name='schedule_meeting', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    expert_name = models.CharField(max_length=255)
    consultation_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    link = models.URLField()
    consultation_package = models.ForeignKey(ConsultationPackage, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    denial_reason = models.TextField(blank=True, null=True)  # Field for the reason of denial
    
    def __str__(self):
        return f"{self.title} with {self.expert_name} on {self.consultation_date}"
    
class InvestmentFunds(models.Model):
    entrepreneur = models.ForeignKey(Registration, related_name='investment_fund', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    industry = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=[
        ('Equity', 'Equity'),
        ('Debt', 'Debt'),
        ('Convertible Note', 'Convertible Note'),
    ])
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    contact_method = models.CharField(max_length=100, choices=[
        ('Email', 'Email'),
        ('Phone', 'Phone'),
    ])
    notes = models.TextField()
    supporting_documents = models.FileField(upload_to='supporting_documents/', null=True, blank=True)

    def __str__(self):
        return self.title


class Investor(models.Model):
    TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('organization', 'Organization'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    
    # Common fields
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    capital = models.CharField(max_length=100)
    information = models.TextField()
    
    # Individual-specific fields
    surname = models.CharField(max_length=100, blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    
    # Organization-specific fields
    company = models.CharField(max_length=100, blank=True, null=True)

    # Investment preferences
    tourism = models.BooleanField(default=False)
    media = models.BooleanField(default=False)
    commercial = models.BooleanField(default=False)
    estate = models.BooleanField(default=False)
    manufacturing = models.BooleanField(default=False)
    education = models.BooleanField(default=False)
    health = models.BooleanField(default=False)
    wholesale = models.BooleanField(default=False)
    user_type = models.CharField(max_length=20, default='investor')

    def __str__(self):
        return f"{self.type} - {self.email}"



class ReplyRequest(models.Model):
    meeting = models.ForeignKey('ScheduledMeeting', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    text_area = models.TextField()
    status_choices = [
        ('SENT', 'Sent'),
        ('NOT_SENT', 'Not Sent'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='NOT_SENT')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
