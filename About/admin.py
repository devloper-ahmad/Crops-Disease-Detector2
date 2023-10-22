from django.contrib import admin
from About.models import About

class AboutAdmin(admin.ModelAdmin):
    list_display=('title_About','desc_About')
    
admin.site.register(About,AboutAdmin)

# Register your models here.
