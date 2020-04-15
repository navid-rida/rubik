from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customer/add', views.CustomerCreateView.as_view(), name='create_customer'),
    path('product/add', views.ProductCreateView.as_view(), name='create_product'),
    path('quotation/add', views.QuotationCreateView.as_view(), name='create_quotation'),
    path('quotation/select_product', views.select_quotation_product, name='select_quotation_product'),
]
