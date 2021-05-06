from django.contrib import admin
from . import models


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("doctor", "patient", 'date', 'time', 'status')


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ("doctor", "patient", 'date')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("user", 'date', 'paid', 'outstanding', 'total', 'payment_type')


admin.site.register(models.Appointment, AppointmentAdmin)
admin.site.register(models.Prescription, PrescriptionAdmin)
admin.site.register(models.Payment, PaymentAdmin)
