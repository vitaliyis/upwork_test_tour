from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):
    #list_display = ["first_name", "last_name", "city"]
    #exclude = []
    list_display = [field.name for field in Client._meta.fields]

    class Meta:
        model = Client

admin.site.register(Client, ClientAdmin)