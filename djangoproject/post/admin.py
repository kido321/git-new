from django.contrib import admin
from .models import Products,Offers,Todo,user,Fb


class ProductsAdminnn(admin.ModelAdmin):
    list_display = ('name','price','stock','image_url')

class OffersAdmin(admin.ModelAdmin):
    list_display = ('discount','any_thing_to_say')
class Todoadmin(admin.ModelAdmin):
    list_display = ('added_date','added_text')


admin.site.register(Products ,ProductsAdminnn)
admin.site.register(Offers,OffersAdmin)
admin.site.register(Todo,Todoadmin)
admin.site.register(user)
admin.site.register(Fb)

