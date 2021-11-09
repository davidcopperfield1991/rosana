from django.contrib import admin

# Register your models here.
from rosana_order.models import OrderDetail, Order

admin.site.register(Order)
admin.site.register(OrderDetail)