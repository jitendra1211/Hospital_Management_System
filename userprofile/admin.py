from django.contrib import admin
from .models import *


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "name", 'phone', 'email', 'gender', 'blood_group', 'status')


admin.site.register(UserProfile, UserProfileAdmin)
