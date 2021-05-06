from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User
from django import forms

ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('usertype',)}),
)


class MyUserCreationForm(UserCreationForm):
    USER_CHOICES = [
        ('D', 'Doctor'),
        ('P', 'Patient'),
        ('R', 'Receptionist'),
        ('HR', 'HR')
    ]
    usertype = forms.TypedChoiceField(choices=USER_CHOICES, widget=forms.RadioSelect, coerce=str)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'usertype')


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        # include = ('usertype',)


class MyUserAdmin(UserAdmin):
    model = User
    # form = MyUserChangeForm
    # add_form = MyUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS


admin.site.register(User, MyUserAdmin)
