from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from rosana_products.models import Product


class Order(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="سفارش دهنده")
    is_paid = models.BooleanField(verbose_name="پرداخت شده / نشده")
    payment_date = models.DateTimeField(blank=True,null=True,verbose_name="تاریخ پرداخت")

    class Meta:
        verbose_name_plural = "سبد های خرید کاربران"
        verbose_name = "سبد خرید"

    def __str__(self):
        return self.owner.username


    def get_total_price(self):
        amount = 0
        for detail in self.orderdetail_set.all():
            amount += detail.price * detail.count
        return amount


class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name=" سفارش ")
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="محصول")
    price = models.IntegerField(verbose_name="مبلغ")
    count = models.IntegerField(verbose_name="تعداد")

    class Meta:
        verbose_name_plural = "اطلاعات جزيیات محصول "
        verbose_name = "جزئیات محصول"


    def __str__(self):
        return self.product.title

    def get_detail_sum(self):
        return self.price * self.count