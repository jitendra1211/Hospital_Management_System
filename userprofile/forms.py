from django import forms
from .models import UserProfile
from appointment.models import Payment


class UserProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=50)

    class Meta:
        model = UserProfile
        exclude = ('user', 'department', 'salary', 'status', 'attendance')


class UserPaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('paid', 'outstanding', 'payment_type')


class DocProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=50)

    class Meta:
        model = UserProfile
        exclude = ('user', 'med_reps', 'case_paper', 'address', 'blood_group')
