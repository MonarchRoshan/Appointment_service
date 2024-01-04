from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor_id', 'patient_id', 'appointment_time', 'purpose', 'sick_information', 'created_at', 'updated_at']
