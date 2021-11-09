from django.urls import path

from rosana_contact.views import contact_page

urlpatterns = [
    path('contact-us',contact_page)


]