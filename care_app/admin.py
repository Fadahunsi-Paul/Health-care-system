from django.contrib import admin
from .model.department import Department
from .model.patient import Patients
from .model.doctor import Doctors
from .model.appointment import Appointment


# Register your models here.
admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(Department)
admin.site.register(Appointment)