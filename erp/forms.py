from .models import Product, QuotationProduct, Quotation
#from django.forms import ModelForm
from django import forms
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *
#from datetime import date, timedelta
#from django.utils import timezone
#from .validators import *
#import floppyforms as floppy
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
#from django.conf import settings
#from django.db import transaction


class ProductSelectForm(forms.Form):
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all())


class QuotationProductForm(forms.ModelForm):
    
    class Meta:
        model = QuotationProduct
        exclude = ()

QuotationProductFormSet = inlineformset_factory(Quotation, QuotationProduct, form= QuotationProductForm, fields=['product', 'unit', 'price'], extra=1, can_delete = True)

class QuotationForm(forms.ModelForm):

    class Meta:
        model = Quotation
        exclude=['product']

    def __init__(self, *args, **kwargs):
        super(QuotationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('shipping_charge'),
                Field('vat_percent'),
                Field('tax_percent'),
                Field('advance_percent'),
                
                
                Fieldset('Add Products',
                    Formset('products')),
                Field('customer'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )