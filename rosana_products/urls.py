from django.urls import path


from .views import products_list , ProductList , product_detail , SearchProductsView , ProductListByCategory , product_categories_partial

urlpatterns = [
    path('products-function', products_list),
    path('products/', ProductList.as_view()),
    path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
    path('products/<category_name>', ProductListByCategory.as_view()),
    path('products_ccategory_partial', product_categories_partial,name="product_categories_partial")


]