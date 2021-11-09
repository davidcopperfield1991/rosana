from django.db import models

# Create your models here.

class ContactUs(models.Model):
    full_name =models.CharField(max_length=50,verbose_name="نام کامل")
    email = models.EmailField(max_length=50,verbose_name="ایمیل")
    subject = models.CharField(max_length=20,verbose_name="عنوان")
    text = models.TextField(verbose_name="متن پیام")
    is_read = models.BooleanField(verbose_name="خوانده شده / خوانده نشده")

    class Meta:
        verbose_name_plural = "ارتباط با ما"
        verbose_name = "تماس با ما"


    def __str__(self):
        return self.subject