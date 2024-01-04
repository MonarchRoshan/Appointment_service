from django.db import models

# Create your models here.


from django.db import models

class Appointment(models.Model):
    appointment_id = models.CharField(max_length=50)
    doctor_id = models.CharField(max_length=50)
    patient_id = models.CharField(max_length=50)
    appointment_time = models.DateTimeField()
    purpose = models.TextField()
    sick_information = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

