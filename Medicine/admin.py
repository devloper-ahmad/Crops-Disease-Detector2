from django.contrib import admin
from Medicine.models import Medicine

class MedicineAdmin(admin.ModelAdmin):
    list_display=('Product_desc','Medicine_title','Pack_size','Composition','Mode_of_action','Formulation','Crops','Pests','Dose','Medicine_img')

admin.site.register(Medicine,MedicineAdmin)

# Register your models here.
