from django.urls import path

from rosana_order.views import add_user_order, user_open_order, verify, send_request , remove_order_detail

urlpatterns = [
    path('add_user_order',add_user_order),
    path('open-order',user_open_order),
    path('remove-order-detail/<detail_id>',remove_order_detail),
    path('request', send_request, name='request'),
    path('verify/<order_id>', verify , name='verify'),


]