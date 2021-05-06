from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', label_suffix='',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', label_suffix='',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserCreateForm(UserCreationForm):
    USER_CHOICES = [
        ('D', 'Doctor'),
        ('P', 'Patient'),
    ]
    usertype = forms.TypedChoiceField(choices=USER_CHOICES, widget=forms.RadioSelect, coerce=str)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'usertype')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field == 'usertype':
                self.fields[field].widget.attrs.update({
                    'class': 'form-check-input'
                })
