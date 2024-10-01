from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone



class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employer', 'Employer'),
        ('passenger', 'Passenger'),
        ('maintenance', 'Maintenance'),
    )
    
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='passenger')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    phone = models.CharField(max_length=15, default='0000000000')  # Provide a default value
    address = models.TextField(null=True, blank=True)  # Temporarily allow null

class Contact(models.Model):
    email = models.EmailField()
    description = models.TextField()
    date = models.DateField(auto_now_add=True)  # Automatically set the date to now
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Route(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DecimalField(max_digits=5, decimal_places=2)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    start_station = models.CharField(max_length=255)
    end_station = models.CharField(max_length=255)
    image = models.ImageField(upload_to='route_images/')

    def __str__(self):
        return self.name



class Ticket(models.Model):
    TOWN_CHOICES = [
        ('Yaoundé', 'Yaoundé'),
        ('Bafoussam', 'Bafoussam'),
        ('Ngaoundéré', 'Ngaoundéré'),
        ('Douala', 'Douala'),
        ('Bamenda', 'Bamenda'),
        ('Garoua', 'Garoua'),
    ]

    CLASSIFICATION_CHOICES = [
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
        ('VIP', 'VIP'),
    ]

    hour = models.TimeField()
    departure = models.CharField(max_length=255, choices=TOWN_CHOICES)
    arrival = models.CharField(max_length=255, choices=TOWN_CHOICES)
    classification = models.CharField(max_length=20, choices=CLASSIFICATION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    railway_name = models.CharField(max_length=255, default='E-railway Railway')

    def __str__(self):
        return f'{self.classification} Ticket: {self.departure} to {self.arrival}'

    def save(self, *args, **kwargs):
        # Automatically set the price based on classification
        if self.classification == 'Standard':
            self.price = 2000
        elif self.classification == 'Premium':
            self.price = 4000
        elif self.classification == 'VIP':
            self.price = 10000

        super().save(*args, **kwargs)



class MaintenanceTask(models.Model):
    TASK_DURATION_CHOICES = (
        ('periodic', 'Periodic'),
        ('monthly', 'Monthly'),
    )

    STATUS_CHOICES = (
        ('not_done', 'Not Done'),
        ('done', 'Done'),
    )

    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'maintenance'})
    task_name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=10, choices=TASK_DURATION_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='not_done')
    assigned_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateField()
    sanction_applied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task_name} assigned to {self.assigned_to.username}"