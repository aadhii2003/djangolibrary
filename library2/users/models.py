from django.contrib.auth.models import AbstractUser

from django.db import models

#
# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    gender= models.CharField(max_length=10)
    email=models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name

# customeuser definition

class CustomUser(AbstractUser):
    address=models.CharField(max_length=20,default="")
    phone=models.IntegerField(default=0)

    is_superuser=models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)

    def __str__(self):
        return self.username