from django.db import models
class disease1(models.Model):
     disease1_title=models.CharField(max_length=50)
     disease1_desc=models.TextField()
     disease1_img=models.FileField(upload_to="medicine2/",max_length=250,null=True, default=None)

# Create your models here.
