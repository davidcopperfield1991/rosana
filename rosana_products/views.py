from django.shortcuts import render
from django.views.generic import ListView

from rosana_order.forms import UserNewOrderForm
from .models import Product, ProductGallery
from django.http import Http404
from rosana_products_category.models import ProductsCategory
import itertools


# Create your views here.


def products_list(request):
    products = Product.objects.get_active_products()
    print(products)
    context = {
        "object": products
    }
    return render(request, "products/product_list_function.html", context)


class ProductList(ListView):
    template_name = "products/products_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()


class ProductListByCategory(ListView):
    template_name = "products/products_list.html"
    paginate_by = 6

    def get_queryset(self):
        print(self.kwargs)
        category_name = self.kwargs["category_name"]
        category = ProductsCategory.objects.filter(name__exact=category_name).first()
        if category is None:
            raise Http404("صفحه مورد نظر یافت نشد")
        return Product.objects.get_products_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e != None] for t in itertools.zip_longest(*args))


def product_detail(request,*args,**kwargs):

    selected_product_Id = kwargs["productId"]

    new_order_form = UserNewOrderForm(request.POST or None , initial={"product_id":selected_product_Id})

    product: Product = Product.objects.get_by_id(selected_product_Id)
    if product is None or not product.active:
        raise Http404("محصول مورد نظر یافت نشد")
    product.visit_count += 1
    product.save()

    related_products = Product.objects.get_queryset().filter(category__product=product).distinct()

    grouped_related_products = my_grouper(3 ,related_products)

    galleries = ProductGallery.objects.filter(product_id=selected_product_Id)
    grouped_galleries =(list(my_grouper(3 ,galleries)))



    context = {
            "product": product ,
            'galeries' : grouped_galleries,
            'related_products' : grouped_related_products,
            "new_order_form" : new_order_form
        }




    return render(request, "products/product_detail.html", context)


class SearchProductsView(ProductList):
    template_name = "products/products_list.html"

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_products()




# تو این کلاس اردوخانی اومده بود از کلاس listview بهش ارث داده بود که مشکل داشت بنظرم من اومدم از این بهش ارث دادم


def product_categories_partial(request):
    category = ProductsCategory.objects.all()
    context = {
        'category' : category
    }
    return render(request, "products/products_category_partial.html", context)
