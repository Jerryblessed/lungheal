from django.contrib import admin

# Register your models here.

from accounts.models import Patientdb

@admin.register(Patientdb)
class PatientModel(admin.ModelAdmin):
    # list_display = ['id','name','email','dob','state','gender','location','pimage','classified','uploaded','phone_number']
    list_display = ('name', 'email', 'dob', 'state', 'gender', 'location', 'phone_number', 'image', 'classified', 'uploaded')