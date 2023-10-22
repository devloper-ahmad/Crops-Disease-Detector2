from django.db import models
from tinymce.models import HTMLField
class About(models.Model):
     title_About=models.CharField(max_length=100)
     desc_About=HTMLField()

def __str__(self):  

 return self.caption

# Create your models here.
