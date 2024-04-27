from django.db import models
from health_care.basemodel import TimeBaseModel
from django.core.validators import RegexValidator
from care_app.utils import GENDER_CHOICES
from django.utils import timezone

class Patients(TimeBaseModel):
    first_name = models.CharField(max_length=100,blank=False)
    second_name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(unique=True) 
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{10,15}$')])
    address = models.TextField()
    image = models.ImageField(null=True,blank=True)

    class Meta:
        verbose_name_plural = 'Patients'

    def __str__(self):
        return self.email
    
    @property
    def imageUrl(self):
        try:
            url=self.image.url
        except:
            url=''
        return url 