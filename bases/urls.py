from django.urls import path
from django.contrib.auth import views as auth_views

from bases.views import Home, Services, Contacts, Shop
urlpatterns = [
    path('',Home.as_view(), name='home'),

    path('shop/', Shop.as_view(),
        name='shop'),
    path('services/', Services.as_view(),
        name='services'),
    path('contacts/', Contacts.as_view(),
        name='contacts'),
]