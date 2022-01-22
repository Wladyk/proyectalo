from django.db import models
from django.contrib.auth.models import User, AbstractUser
#Inherits from Abstract elemental class
class User(AbstractUser):
    ideologistFlag = models.BooleanField(default=False)
    builderFlag = models.BooleanField(default=False)
    profilePicture = models.ImageField(default="")
    REQUIRED_FIELDS = ['ideologistFlag','builderFlag','first_name','last_name','email']
class Technology(models.Model):
    name = models.CharField(max_length=200)
    class Meta:
        verbose_name = "Technologie" #Just for the sake of the plural written form on the admin panel

class Ideologist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "Ideologist"

class Builder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    technologies = models.ManyToManyField(Technology, through="TechnologyBuilder")
    # The m2m field has been dealt with in a traditional, non-Django dependent way by creating a separate intersection entity
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = "Builder"
class TechnologyBuilder(models.Model):
    class SkillLevel(models.IntegerChoices):
        IMMATERIAL = 1
        TANGIBLE = 2
        SOLID = 3
        POWERFUL = 4

    skill = models.IntegerField(choices=SkillLevel.choices)
    technology = models.ForeignKey(Technology, on_delete=models.DO_NOTHING)
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)

class Project(models.Model):
    class ConstructionStage(models.IntegerChoices):
        ROUGH = 1,
        SHAPED = 2,
        POLISHED = 3,
        JEWEL = 4
    ideologist = models.ForeignKey(Ideologist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    interestRating = models.IntegerField()
    technologies = models.ManyToManyField(Technology)
    interested = models.ManyToManyField(Builder, through="InterestProjectBuilder", related_name="IntProjBuil")
    builders = models.ManyToManyField(Builder, through="ProjectBuilder", related_name="projBuild")
    budget = models.FloatField()
    timeBurden = models.IntegerField()
    stage = models.IntegerField(choices=ConstructionStage.choices)
    
class ProjectBuilder(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    builder = models.ForeignKey(Builder, on_delete=models.DO_NOTHING)
    initialDate = models.DateField(default=None)
    endDate = models.DateField(default=None)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="senderUser")
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="receiverUser")
    body = models.TextField(default="Hi! I'm sending you this message")
    date = models.DateTimeField(default=None)
  
#class TechnologyProject(models.Model):
#    technologie = models.ForeignKey(Technology, on_delete=models.DO_NOTHING)
#    project = models.ForeignKey(Project, on_delete=models.CASCADE)
class Match(models.Model):
    ideologist = models.ForeignKey(Ideologist, on_delete=models.CASCADE)
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
    date = models.DateField(default=None)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
class InterestProjectBuilder(models.Model ):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    builder = models.ForeignKey(Builder, on_delete=models.CASCADE)
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
    number = models.IntegerField()
    floor = models.IntegerField()
    apartment = models.CharField(max_length=1)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE) 





    
# Create your models here.
