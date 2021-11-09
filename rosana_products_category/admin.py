from django.contrib import admin

# Register your models here.
from .models import ProductsCategory


class productCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', "name" ]

    class Meta:
        model = ProductsCategory


admin.site.register(ProductsCategory , productCategoryAdmin)