from django.db import models

# Create your models here.


class ProductsCategory(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان")
    name = models.CharField(max_length=50,verbose_name="عنوان در url")

    class Meta:
        verbose_name_plural = " دسته بندی ها  "
        verbose_name = "دسته بندی"

    def __str__(self):
        return self.title