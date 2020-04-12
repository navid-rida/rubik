from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic.edit import CreateView
from .models import Customer, Product, Quotation


# Create your views here.
@login_required
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    context = {'testdata': "This is just for testing"}
    return render(request, 'erp/base.html', context)


#@login_required
class CustomerCreateView(CreateView):
    model=Customer
    template_name_suffix = '_create_form'
    fields=['name','email','cell','address','comment']
    success_url= reverse_lazy('create_customer')


class ProductCreateView(CreateView):
    model=Product
    template_name_suffix = '_create_form'
    fields=['name','paper_material','height','width','length','color_number']
    success_url= reverse_lazy('create_product')


class QuotationCreateView(CreateView):
    model=Quotation
    template_name = 'erp/quotation/quotation_create_form.html'
    fields=['product','shipping_charge','vat_percent','tax_percent','advance','later_payment', 'customer']
    success_url= reverse_lazy('create_quotation')