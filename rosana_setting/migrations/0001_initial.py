# Generated by Django 3.1.4 on 2021-01-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('address', models.CharField(max_length=100, verbose_name='آدرس')),
                ('phone', models.CharField(max_length=100, verbose_name='شماره')),
                ('mobile', models.CharField(max_length=100, verbose_name='همراه')),
                ('fax', models.CharField(max_length=100, verbose_name='فکس')),
                ('email', models.EmailField(max_length=100, verbose_name='ایمیل')),
                ('about_us', models.CharField(max_length=100, verbose_name='درباره ما')),
                ('copy_right', models.CharField(max_length=100, verbose_name='کپی رایت')),
            ],
            options={
                'verbose_name': 'تنظیمات',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]