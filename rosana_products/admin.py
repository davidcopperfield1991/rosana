from django.contrib import admin

# Register your models here.

from .models import Product , ProductGallery


class productAdmin(admin.ModelAdmin):
    list_display = ['__str__', "title" , "price" , "active"]

    class Meta:
        model = Product


admin.site.register(Product , productAdmin)
admin.site.register( ProductGallery)