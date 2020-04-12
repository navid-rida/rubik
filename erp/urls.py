from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/customer', views.CustomerCreateView.as_view(), name='create_customer'),
    path('add/product', views.ProductCreateView.as_view(), name='create_product'),
    path('add/quotation', views.QuotationCreateView.as_view(), name='create_quotation'),
]
