from django.contrib import admin
from ship.models import ship

class shipAdmin(admin.ModelAdmin):
    list_display=('First_Name','Last_Name','Email','Address','city','state','Postal_code','Select_Medicine','Payment')

admin.site.register(ship,shipAdmin)

# Register your models here.
