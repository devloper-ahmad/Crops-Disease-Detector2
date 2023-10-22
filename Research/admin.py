from django.contrib import admin
from Research.models import Research

class ResearchAdmin(admin.ModelAdmin):
     list_display=('title_Research','desc_Research','img_Research')

admin.site.register(Research,ResearchAdmin)

# Register your models here.
