from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor')

    def __str__(self):
        return "Patient - {} Doc- {} At {} {}".format(self.patient, self.doctor, self.date, self.time)


class Prescription(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_prescription')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_prescription')
    date = models.DateField(auto_now_add=True)
    symptoms = models.CharField(max_length=200)
    prescription = models.TextField()

    def __str__(self):
        return "Prescription Doc - {} Patient - {}".format(self.doctor, self.patient)


PAYMENT_TYPES = [
    ('I', 'Individual'),
    ('C', 'Consulting')
]


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patient_payments")
    date = models.DateField(auto_now_add=True)
    paid = models.IntegerField(null=True)
    outstanding = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    payment_type = models.CharField(choices=PAYMENT_TYPES, max_length=1, default="I")

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return "Payment User-{} Amount-{}".format(self.user, self.total)
