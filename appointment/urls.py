from django.urls import path
from .views import *

urlpatterns = [
    path('appointment/p/', AppointmentForAPatientView.as_view(), name="patient_appointment"),
    path('appointment/d/', AppointmentForADoctorView.as_view(), name="doctor_appointment"),
    path('appointment/create/', appointment_create_view, name="appointmentCreate"),
    path('appointment/d/update/<int:pk>', appointment_update_pk, name="appointment_update_pk"),
    path("medHistory/", MedicalHistoryView.as_view(), name="med-history"),
    path('prescriptions/', PrescriptionListView.as_view(), name="doc-prescriptions"),
    path('prescriptions/create', prescription_create_view, name="doc-prescriptions-create"),
    path("rdashboard/", rdashboard, name="r_dashboard"),
    path("hrdashboard/", hrdashboard, name="hr_dashboard"),
]