from django.db import models
from health_care.basemodel import TimeBaseModel
from django.core.validators import RegexValidator
from care_app.utils import GENDER_CHOICES
from django.utils import timezone
from datetime import date

class Patients(TimeBaseModel):
    first_name = models.CharField(max_length=100,blank=False)
    second_name = models.CharField(max_length=100,blank=False)
    email = models.EmailField(unique=True) 
    date_of_birth = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12, validators=[RegexValidator(r'^\d{10,15}$')])
    address = models.TextField()
    image = models.ImageField(null=True,blank=True)

    

    class Meta:
        verbose_name_plural = 'Patients'

    def __str__(self):
        return self.email


    def age(self):
        try:
            today = date.today()
            date_of_birth = self.date_of_birth
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            return age
        except ValueError:
            return None

    @property
    def imageUrl(self):
        try:
            url=self.image.url
        except:
            url=''
        return url 