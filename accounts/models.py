from django.db import models

from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save

class UserModel(AbstractUser):

    phone = models.CharField(max_length=100,unique=True)

class UserProfileModel(models.Model):

    skill = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    linkedin_url = models.URLField(null=True)

    github_url = models.URLField(null=True)

    owner = models.OneToOneField(UserModel,on_delete=models.CASCADE)    


def create_profile(sender,instance,created,*args,**kwargs):

    if created:

        UserProfileModel.objects.create(owner=instance)

post_save.connect(create_profile,sender=UserModel)