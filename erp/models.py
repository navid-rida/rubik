from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Customer(models.Model):
    #cus_id = models.CharField('Customer ID (Auto)', max_length=11)
    name = models.CharField('Name of Customer', max_length=100)
    email = models.EmailField('Email of the Customer')
    cell = models.CharField('Contact Number', max_length=11, validators=[RegexValidator(regex='^[0-9]*$', message='Must be number')])
    address = models.TextField('Shipping Address', max_length=300)
    comment = models.CharField(max_length=300)

    def __str__(self):
        return self.name+" "+self.cell


class Product(models.Model):
    name  = models.CharField('Product Name', max_length=50)
    paper_material = models.CharField('Paper material', max_length=50)
    height = models.DecimalField('Height (in inch)', max_digits = 4, decimal_places = 2)
    width = models.DecimalField('Width (in inch)', max_digits = 4, decimal_places = 2)
    length = models.DecimalField('Length (in inch)', max_digits = 4, decimal_places = 2)
    color_number = models.IntegerField('Number of Printer Colors') # Restrict to 12 in validation

    def __str__(self):
        return self.name

class Quotation(models.Model):
    product = models.ManyToManyField(Product, through='QuotationProduct')
    shipping_charge = models.DecimalField('Shipping Charge', max_digits=20, decimal_places=2)
    vat_percent = models.DecimalField('Vat (Percent)', max_digits=5, decimal_places=2)
    tax_percent = models.DecimalField('Tax (Percent)', max_digits=5, decimal_places=2)
    advance = models.DecimalField('Advance Payment', max_digits=20, decimal_places=2)
    later_payment = models.DecimalField('To be paid later', max_digits=20, decimal_places= 2)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)


class QuotationProduct(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quotation = models.ForeignKey(Quotation, on_delete= models.CASCADE)
    unit = models.IntegerField('Unit')
    price = models.DecimalField('Unit Price (BDT)', max_digits=20, decimal_places=2)
