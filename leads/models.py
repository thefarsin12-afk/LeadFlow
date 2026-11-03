from django.db import models

from accounts.models import UserModel

class Lead(models.Model):

    SOURCE_CHOICES = {
    
            ("Website","Website"),
            ("Social Media","Social Media"),
            ("Referral","Referral"),
            ("Advertisement","Advertisement"),
            ("Other","Other"),
        }

    STATUS_CHOICES = {
    
            ("New","New"),
            ("Contacted","Contacted"),
            ("Interested","Interested"),
            ("Converted","Converted"),
            ("Lost","Lost"),
        }

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=100,unique=True)

    company = models.CharField(max_length=200,null=True,blank=True)

    source = models.CharField(max_length=100,choices=SOURCE_CHOICES,default="Website")
    
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default="Interested")

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(UserModel,on_delete=models.CASCADE)

    def __str__(self):

        return self.name