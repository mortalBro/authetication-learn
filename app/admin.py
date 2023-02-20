from django.contrib import admin
from .models import Employe

# Register your models here.
@admin.register(Employe)

class EmployeAdmin(admin.ModelAdmin):
    list_display = ['id','name','adress','phone']