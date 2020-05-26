from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.decorators import login_required,user_passes_test

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import *
from django.db import transaction

from django.contrib.messages.views import SuccessMessageMixin

from .forms import *

from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from pathlib import Path

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
    fields= '__all__'
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
    #success_url= reverse_lazy('show_quotation_template', kwargs={'pk': self.object.id})
    success_message = "A quotation was created successfully with Serial No: %(id)s "

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            id = self.object.id,
        )

    def get_success_url(self):
        return reverse_lazy('show_quotation_template', kwargs={'pk': self.object.id})

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

class QuotationListView(SuccessMessageMixin, ListView):
    model=Quotation
    paginate_by = 100  # if pagination is desired
    template_name = 'erp/quotation/quotation_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class QuotationDownloadView(DetailView):
    model = Quotation
    template_name = 'erp/quotation/quotation_preview.html'


def download_quotation(request, pk):
    quotation = get_object_or_404(Quotation, pk=pk)
    context = {'quotation': quotation}
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = "inline; filename={date}-{name}-quotation.pdf".format(
        date=timezone.now(),
        name=quotation.customer.name,
    )
    html = render_to_string("erp/quotation/quotation_download.html", context)
    #result = rem.pay_previously_unpaid_cash_incentive()
    #return render(request, 'rem/detail/trm.html', context)

    font_config = FontConfiguration()
    #css_path = Path(settings.STATIC_ROOT,'css/bootstrap/bootstrap.css')
    css_path = Path(settings.STATIC_ROOT,'assets/vendor/bootstrap/css/bootstrap.min.css')
    css = CSS(css_path)
    HTML(string=html).write_pdf(response, stylesheets=[css], font_config=font_config)
    return response

"""def select_quotation_product(request):
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
        return render(request,'erp/quotation/quotation_create_form.html', context)"""
