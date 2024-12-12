from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# class School(models.Model):

#     school_name = models.CharField("School Name", max_length=256, blank=False, unique=True)
#     district = models.CharField("District", max_length=256, blank=False)
#     school_address = models.CharField("Address", max_length=256)
#     principal = models.CharField("Principal Name", max_length=256, blank=False)
#     principal_phone = models.CharField("Emergency Contact Phone Number", max_length=256, blank=False)

#     def __str__(self):
#         return f"{self.school_name}"


class CustomUser(AbstractUser):
    username = None
    # school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True)
    email = models.EmailField("email address", unique=True)
    advisor_name = models.CharField("Advisor Name", max_length=256, blank=False)
    advisor_phone_number = models.CharField("Advisor Phone Number", max_length=256, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
