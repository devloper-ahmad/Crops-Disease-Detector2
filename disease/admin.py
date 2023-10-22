from django.contrib import admin
from disease.models import disease
class diseaseAdmin(admin.ModelAdmin):
    list_display=('disease_title','disease_desc','disease_img')

admin.site.register(disease,diseaseAdmin)

# Register your models here.
