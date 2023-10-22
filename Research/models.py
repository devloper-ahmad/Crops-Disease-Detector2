from django.db import models
from tinymce.models import HTMLField
class Research(models.Model):
     title_Research=models.CharField(max_length=100)
     desc_Research=HTMLField()
     img_Research=models.FileField(upload_to="medicine2/",max_length=250, null=True,default=None)

def __str__(self):  

 return self.caption
# Create your models here.
