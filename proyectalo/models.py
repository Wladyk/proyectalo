from django.db import models
from django.contrib.auth.models import User
class Seeker(User):
    def __str__():
        return ""
    class Meta:
        verbose_name = "Seeker"
    
class Offerer(User):
    def __str__():
        return ""
    class Meta:
        verbose_name = "Offerer"

    

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


class Address():
    street = models.CharField(max_length=200)
    number = models.IntegerField(max_length=100)
    floor = models.IntegerField(max_length=1)
    apartment = models.CharField(max_length=1)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE) 





    
# Create your models here.
