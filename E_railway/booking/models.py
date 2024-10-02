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



class Task(models.Model):
    TASK_TYPE_CHOICES = (
        ('periodic', 'Periodic'),
        ('monthly', 'Monthly'),
    )
    STATUS_CHOICES = (
        ('done', 'Done'),
        ('not_done', 'Not Done'),
    )
    SANCTION_CHOICES = (
        ('none', 'None'),
        ('warning', 'Warning'),
        ('temporary_ban', 'Temporary Ban'),
    )

    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'employer'})
    name = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=20, choices=TASK_TYPE_CHOICES)
    ticket_quota = models.IntegerField()
    is_on_guard = models.BooleanField(default=False)  # Whether the user is on guard duty
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_done')
    sanction = models.CharField(max_length=20, choices=SANCTION_CHOICES, default='none')
    assigned_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.assigned_to.username}"

class Communication(models.Model):
    DESTINATION_CHOICES = (
        ('employer', 'Employer'),
        ('maintenance', 'Maintenance'),
        ('passenger', 'Passenger'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='communications/', blank=True, null=True)
    destination = models.CharField(max_length=30, choices=DESTINATION_CHOICES)

    def __str__(self):
        return self.name

class Rating(models.Model):
    rated_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings')
    rating_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

class Report(models.Model):
    reported_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reports')
    reporting_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)


class TicketBought(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('paid', 'Paid'), ('reserved', 'Reserved')])
    date = models.DateTimeField(auto_now_add=True)
