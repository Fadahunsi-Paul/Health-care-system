from django.db import models
from health_care.basemodel import TimeBaseModel
from .doctor import Doctors


class Department(TimeBaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    head_of_department = models.ForeignKey('Doctors', on_delete=models.CASCADE)

    
    

    def __str__(self):
        return self.name
    