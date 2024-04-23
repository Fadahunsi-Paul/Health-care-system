from django.contrib.auth.models import BaseUserManager ,PermissionsMixin 
from django.utils.translation import gettext_lazy as _ 

class CustomUserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if '@'not in email  or '.com' not in  email:
            raise ValueError(_("Email should contain @ or .com"))
        if not email:
            raise ValueError(_("Email should not be blank"))
        if not password:
            raise ValueError(_("Password Feild should not be blank"))
        if len(password)<8:
            raise ValueError(_("Password should contain 8 or more Characters"))
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user  

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)