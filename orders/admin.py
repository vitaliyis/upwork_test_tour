from django.contrib import admin
from .models import *

class ClientInOrderInline(admin.TabularInline):
    model = ClientInOrder
    extra = 0

class StatusOrderAdmin(admin.ModelAdmin):
    #list_display = ["first_name", "last_name", "city"]
    #exclude = []
    list_display = [field.name for field in StatusOrder._meta.fields]

    class Meta:
        model = StatusOrder

admin.site.register(StatusOrder, StatusOrderAdmin)

class PeriodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Period._meta.fields]

    class Meta:
        model = Period

admin.site.register(Period, PeriodAdmin)

class OrderAdmin(admin.ModelAdmin):
    inlines = [ClientInOrderInline]
    list_display = [field.name for field in Order._meta.fields]
    exclude = ("amount",)
    readonly_fields = ('amount',)

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)