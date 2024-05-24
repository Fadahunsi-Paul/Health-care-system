from django.db import models
from .model.doctor import Doctors
from health_care.basemodel import TimeBaseModel
from care_app.utils import DOC_STATUS

class Schedule(TimeBaseModel):
    doctor_name = models.ForeignKey(Doctors, models.CASCADE)
    days = models.CharField(max_length=50)
    start_time = models.TimeField(default='00:00')
    end_time = models.TimeField(default='00:00')
    message = models.TextField()
    status = models.CharField(max_length=50,choices=DOC_STATUS)

    def __str__(self):
        return self.doctor_name
