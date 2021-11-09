import os

from django.db import models

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"logo/{final_name}"


class SiteSetting(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان")
    address = models.CharField(max_length=100,verbose_name="آدرس")
    phone = models.CharField(max_length=100,verbose_name="شماره")
    mobile = models.CharField(max_length=100,verbose_name="همراه")
    fax = models.CharField(max_length=100,verbose_name="فکس")
    email = models.EmailField(max_length=100,verbose_name="ایمیل")
    about_us = models.CharField(max_length=100,verbose_name="درباره ما")
    copy_right = models.CharField(max_length=100,verbose_name="کپی رایت")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name="تصویر لوگو")

    class Meta:
        verbose_name_plural = "تنظیمات سایت"
        verbose_name = "تنظیمات"


    def __str__(self):
        return self.title