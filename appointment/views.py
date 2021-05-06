from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import *
from userprofile.models import UserProfile
from .forms import *


class AppointmentForAPatientView(ListView):
    login_url = '/login'
    redirect_field_name = 'account: login'

    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)


class AppointmentForADoctorView(ListView):
    login_url = '/login'
    redirect_field_name = 'account: login'

    def get_queryset(self):
        return Appointment.objects.filter(doctor=self.request.user, status='Pending')


class MedicalHistoryView(ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        return Prescription.objects.filter(patient=self.request.user).order_by('-date')


class PrescriptionListView(ListView):
    login_url = '/login/'
    redirect_field_name = 'account:login'

    def get_queryset(self):
        return Prescription.objects.filter(doctor=self.request.user).order_by('-date')


def prescription_create_view(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user
            prescription.save()
            return redirect('doc-prescriptions')
    else:
        form = PrescriptionForm()
    return render(request, 'appointment/prescription_create.html', {'form': form})


def appointment_create_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.save()
            return redirect('r_dashboard')
    else:
        form = AppointmentForm()
    return render(request, 'appointment/appointment_create.html', {'form': form})


def appointment_update_pk(request, pk):
    if request.method == 'POST':
        appointment = Appointment.objects.get(pk=pk)
        appointment.status = 'Completed'
        appointment.save()
    return redirect('doctor_appointment')


def rdashboard(request):
    if request.method == "GET" and request.user.usertype == "R":
        context = {
            "totalApp": len(Appointment.objects.all()),
            "compApp": len(Appointment.objects.filter(status="Completed")),
            "pendApp": len(Appointment.objects.filter(status="Pending")),
            "app_list": Appointment.objects.all(),
            "pat_list": UserProfile.objects.filter(user__usertype="P")[0:5]
        }
        return render(request, 'appointment/r_dashboard.html', context=context)


# @login_required(login_url='/login/')
def hrdashboard(request):
    if request.method == "GET" and request.user.usertype == "HR":
        context = {
            "totalPat": len(User.objects.filter(usertype="P")),
            "totalDoc": len(User.objects.filter(usertype="D")),
            "onDutyDoc": len(UserProfile.objects.filter(status="Active").filter(user__usertype="D")),
            "doc_list": UserProfile.objects.filter(user__usertype="D")
        }
        return render(request, 'appointment/hr_dashboard.html', context=context)


# @login_required(login_url='/login/')
def hraccounting(request):
    if request.method == "GET" and request.user.usertype == "HR":
        context = {
            "payment_ind": Payment.objects.filter(payment_type="I"),
            "payment_cons": Payment.objects.filter(payment_type="C"),
        }
        return render(request, 'appointment/accounting.html', context=context)


# @login_required(login_url='/login/')
def pateintpayments(request):
    if request.method == "GET":
        context = {
            "payment_me": Payment.objects.filter(user=request.user),
        }
        return render(request, 'appointment/payment_invoice.html', context=context)