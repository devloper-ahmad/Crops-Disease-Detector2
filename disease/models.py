from django.db import models
class disease(models.Model):
    disease_title=models.CharField(max_length=50)
    disease_desc=models.TextField()
    disease_img=models.FileField(upload_to="medicine2/",max_length=250,null=True, default=None)

# Create your models here.
