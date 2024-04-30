from health_care.basemodel import TimeBaseModel
from django.db import models
from django.core.validators import RegexValidator
from care_app.utils import GENDER_CHOICES
from django.utils import timezone

class Doctors(TimeBaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,blank=True) 
    date_of_birth = models.DateField(default=timezone.now) 
    specialty = models.ForeignKey('Department', on_delete = models.CASCADE)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,validators=[RegexValidator(r'^\d{10,15}$')])
    image = models.ImageField(upload_to='doc-pics/',blank=True,null =True) 

    class Meta:
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return self.email

    @property
    def imageUrl(self):
        try:
            url=self.image.url
        except:
            url=''
        return url 
