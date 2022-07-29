from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    Address=models.TextField()
    Email=models.EmailField()
    Phone_Number=models.CharField(max_length=12,null=True)
    Gender=models.CharField(max_length=7,null=True)
    nationality=models.CharField(max_length=15,null=True)
    Age=models.IntegerField()