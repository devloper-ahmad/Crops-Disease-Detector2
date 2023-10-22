from django.db import models

class ship(models.Model):
    First_Name=models.CharField(max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Address=models.TextField()
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    Postal_code=models.CharField(max_length=50)
    Select_Medicine=models.CharField(max_length=50)
    Payment=models.CharField(max_length=50)


# Create your models here.
