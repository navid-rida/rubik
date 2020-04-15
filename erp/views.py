from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,user_passes_test

from django.views.generic.edit import CreateView, UpdateView
from .models import *
from django.db import transaction

from .forms import *

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
    #fields=['shipping_charge','vat_percent','tax_percent','advance','later_payment', 'customer']
    form_class = QuotationForm
    success_url= reverse_lazy('create_quotation')

    def get_context_data(self, **kwargs):
        data = super(QuotationCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['products'] = QuotationProductFormSet(self.request.POST)
        else:
            data['products'] = QuotationProductFormSet()
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        products = context['products']
        with transaction.atomic():
            self.object = form.save()
            if products.is_valid():
                products.instance = self.object
                products.save()
        return super(QuotationCreateView, self).form_valid(form)



def select_quotation_product(request):
    if request.method== "POST":
        pform = ProductSelectForm(request.POST)
        if pform.is_valid():
            products = pform.cleaned_data['products']
            context = {'pform': pform, 'products': products}
            return render(request,'erp/quotation/quotation_create_form.html', context)
        else:
            context = {'pform': pform}
            return render(request,'erp/quotation/quotation_create_form.html', context)
    else:
        pform = ProductSelectForm()
        context = {'pform': pform}
        return render(request,'erp/quotation/quotation_create_form.html', context)
