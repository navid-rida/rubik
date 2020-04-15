from django.contrib import admin
from .models import Customer, Product, Quotation, QuotationProduct

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Quotation)
admin.site.register(QuotationProduct)