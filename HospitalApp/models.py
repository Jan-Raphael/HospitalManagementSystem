from django.db import models
from django.contrib.auth.models import User


class PatientAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields specific to patients here
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class DoctorAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    qualification = models.TextField(blank=True, null=True)
    years_of_experience = models.PositiveIntegerField()
    is_doctor = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    patient = models.ForeignKey(PatientAccount, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorAccount, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')

    def __str__(self):
        return f"Appointment {self.id} - {self.patient} with {self.doctor} on {self.appointment_date} at {self.appointment_time}"