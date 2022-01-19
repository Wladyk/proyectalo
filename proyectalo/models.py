from django.db import models
from django.contrib.auth.models import User, AbstractUser
class User(AbstractUser):
    seekerFlag = models.BooleanField(default=False)
    offererFlag = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['seekerFlag','offererFlag']
class Seeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__():
        return ""
    class Meta:
        verbose_name = "Seeker"
    
class Offerer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__():
        return ""
    class Meta:
        verbose_name = "Offerer"


class Project(models.Model):
    name = models.CharField(max_length=200)

class Interest(models.Model ):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    offerer = models.ForeignKey(Offerer, on_delete=models.CASCADE)
    date = models.DateTimeField(default=None)

class State(models.Model):
    name = models.CharField(max_length=200)

class Locality(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

class ZipCode(models.Model):
    code = models.CharField(max_length=200)
    
class Neighborhood(models.Model):
    name = models.CharField(max_length=200)
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE) 
    zipCode = models.ForeignKey(ZipCode, on_delete=models.CASCADE)


class Address(models.Model):
    street = models.CharField(max_length=200)
    number = models.IntegerField(max_length=100)
    floor = models.IntegerField(max_length=1)
    apartment = models.CharField(max_length=1)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE) 





    
# Create your models here.
