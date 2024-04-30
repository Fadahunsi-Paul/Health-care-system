from django.db import models
from django.core.validators import RegexValidator
from .doctor import Doctors
from .patient import Patients
from health_care.basemodel import TimeBaseModel
from .department import Department
from care_app.utils import STATUS_CHOICES

class Appointment(TimeBaseModel):
    apppointment_id = models.CharField(max_length=100,blank=False,unique=True,null=False,default='A000')
    patient = models.ForeignKey(Patients, models.CASCADE) 
    doctor = models.ForeignKey(Doctors, on_delete=models.PROTECT)
    date = models.DateTimeField() 
    phone_number = models.CharField(max_length=15)
    reason = models.TextField() 
    time = models.TimeField(default='00:00')
    statu = models.CharField(max_length=20, choices=STATUS_CHOICES)
    department_of_appointment = models.ForeignKey(Department, models.CASCADE)

    def __str__(self):
        return self.apppointment_id
    