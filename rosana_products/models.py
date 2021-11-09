from django.db import models
import os
from django.db.models import Q

from rosana_products_category.models import ProductsCategory


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"product/{final_name}"

def upload_gallery_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"product/galleries/{final_name}"



# Create your models here.

class ProductsManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self,productId):
        qs = self.get_queryset().filter(id = productId)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search(self , query):
        lookup = (
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__title__icontains=query)
        )
        return self.get_queryset().filter(lookup,active=True).distinct()

    def get_products_by_category(self,category_name):
        return self.get_queryset().filter(category__name__exact=category_name,active=True)




class Product(models.Model):
    title = models.CharField(max_length=20 ,verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    price = models.IntegerField(verbose_name="قیمت")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True,verbose_name="تصویر")
    active = models.BooleanField(default=False,verbose_name="فعال/غیرفعال")
    category = models.ManyToManyField(ProductsCategory,blank=True,verbose_name="دسته بندی")
    visit_count = models.IntegerField(default=0,verbose_name="تعداد بازدید")

    objects = ProductsManager()

    class Meta:
        verbose_name_plural = "محصولات"
        verbose_name = "محصول"


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f"/products/{self.id}/{self.title.replace(' ' ,'-')}"


class ProductGallery(models.Model):
    title = models.CharField(max_length=20, verbose_name="عنوان")
    image = models.ImageField(upload_to=upload_gallery_image_path, verbose_name="تصویر")
    product = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name="محصول")

    class Meta:
        verbose_name_plural = " تصاویر"
        verbose_name = "تصویر"


    def __str__(self):
        return self.title

