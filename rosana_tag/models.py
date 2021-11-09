from django.db import models
from django.db.models.signals import pre_save , post_save

from rosana_products.models import Product
from .utils import unique_slug_generator


class Tag(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان")
    slug = models.SlugField(verbose_name="عنوان در سایت")
    timestamp = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ درج")
    active = models.BooleanField(default=True,verbose_name="فعال/غیرفعال")
    products = models.ManyToManyField(Product,blank=True,verbose_name="محصولات")


    class Meta:
        verbose_name_plural = "برچسب ها"
        verbose_name = "برچسب"




    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender , instance , *args , **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver,sender=Tag)