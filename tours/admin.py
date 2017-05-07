from django.contrib import admin
from .models import *

class TourAdmin(admin.ModelAdmin):
    #list_display = ["first_name", "last_name", "city"]
    #exclude = []
    list_display = [field.name for field in Tour._meta.fields]

    class Meta:
        model = Tour

admin.site.register(Tour, TourAdmin)