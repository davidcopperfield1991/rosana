import itertools

from django.shortcuts import render, redirect

from rosana_products.models import Product
from rosana_setting.models import SiteSetting
from rosana_sliders.models import Sliders


def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        "site_setting": site_setting
    }
    return render(request, 'shared/Header.html', context)


def home_page(request):
    most_visit_product = Product.objects.order_by("-visit_count").all()[:8]
    latest_products = Product.objects.order_by("-id").all()[:8]
    sliders = Sliders.objects.all()
    context={
        "data" : "new data",
        "sliders" : sliders,
        "most_visit" : my_grouper(4,most_visit_product),
        "latest_products" : my_grouper(4,latest_products)
    }
    return render(request,"home_page.html",context)


def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        "site_setting" : site_setting
    }
    return render(request, 'shared/Footer.html',context)

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e != None] for t in itertools.zip_longest(*args))


def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        "site_setting": site_setting
    }
    return render(request, 'about_page.html', context)
