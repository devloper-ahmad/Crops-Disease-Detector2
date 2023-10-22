from django.contrib import admin
from disease1.models import disease1
class disease1Admin(admin.ModelAdmin):
     list_display=('disease1_title','disease1_desc','disease1_img')
    
admin.site.register(disease1,disease1Admin)

# Register your models here.
