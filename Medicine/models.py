from django.db import models

class Medicine(models.Model):
     Product_desc=models.TextField()
     Medicine_title=models.CharField(max_length=50)
     Pack_size=models.CharField(max_length=50)
     Composition=models.CharField(max_length=50)
     Mode_of_action=models.CharField(max_length=50)
     Formulation=models.CharField(max_length=50)
     Crops=models.CharField(max_length=50)
     Pests=models.CharField(max_length=50)
     Dose=models.CharField(max_length=50)
     Medicine_img=models.FileField(upload_to="medicine2/",max_length=250,null=True, default=None)
     



# Create your models here.
