from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/customer', views.CustomerCreateView.as_view(), name='create_customer'),
]
