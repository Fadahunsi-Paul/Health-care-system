from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .usermanager import CustomUserManager 
# Create your models here.

class User(AbstractUser):
    username=None
    email=models.EmailField(blank=False,null=False,unique=True)
    password=models.CharField(_('Email Address'),max_length=100, null=False,blank=False)

    is_staff = models.BooleanField(_('Staff Status'),default=False)
    is_superuser = models.BooleanField(_('Superuser Status'),default=False)
    is_active = models.BooleanField(_('Active User'),default=True)
    email_verified = models.BooleanField(_('Email Verification'),default=True)

    date_joined = models.DateTimeField(_("Date joined"),auto_now_add=True)
    last_joined = models.DateTimeField(_("Last joined"), auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email if self.email else ""
    
