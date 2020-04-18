from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,user_passes_test

from django.views.generic.edit import CreateView, UpdateView
from .models import *
from django.db import transaction

from django.contrib.messages.views import SuccessMessageMixin

from .forms import *

# Create your views here.
@login_required
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    context = {'testdata': "This is just for testing"}
    return render(request, 'erp/base.html', context)


#@login_required
class CustomerCreateView(SuccessMessageMixin, CreateView):
    model=Customer
    template_name = 'erp/customer/customer_create_form.html'
    fields=['name','email','cell','address','comment']
    success_message = "Customer %(name)s was created successfully with ID No: %(id)s "
    success_url= reverse_lazy('create_customer')

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
            id = self.object.id,
        )

class ProductCreateView(SuccessMessageMixin, CreateView):
    model=Product
    template_name = 'erp/product/product_create_form.html'
    fields=['name','paper_material','height','width','length','color_number']
    success_url= reverse_lazy('create_product')
    success_message = "Product %(name)s was created successfully with ID No: %(id)s "

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            name=self.object.name,
            id = self.object.id,
        )
    


class QuotationCreateView(SuccessMessageMixin, CreateView):
    model=Quotation
    template_name = 'erp/quotation/quotation_create_form.html'
    #fields=['shipping_charge','vat_percent','tax_percent','advance','later_payment', 'customer']
    form_class = QuotationForm
    success_url= reverse_lazy('create_quotation')
    success_message = "A quotation was created successfully with Serial No: %(id)s "

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            id = self.object.id,
        )

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
