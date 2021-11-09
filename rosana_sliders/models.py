import os

from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"product/{final_name}"


class Sliders(models.Model):
    title = models.CharField(max_length=100,verbose_name="عنوان")
    linkurl = models.URLField(verbose_name="آدرس")
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True, verbose_name="تصویر")


    class Meta:
        verbose_name_plural = "اسلایدر ها"
        verbose_name = "اسلایدر"




    def __str__(self):
        return self.title