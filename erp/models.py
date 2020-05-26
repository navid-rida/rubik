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
    name  = models.CharField('Product Name', max_length=100)
    paper_material = models.CharField('Paper material', max_length=100)
    height = models.DecimalField('Height (in inch)', max_digits = 4, decimal_places = 2)
    width = models.DecimalField('Width (in inch)', max_digits = 4, decimal_places = 2)
    length = models.DecimalField('Length (in inch)', max_digits = 4, decimal_places = 2)
    color_number = models.IntegerField('Number of Printer Colors') # Restrict to 12 in validation
    dye_cutting = models.BooleanField('Dye Cutting')
    COATED_CHOICES = (('ML', 'Matt Lamination'),
                      ('MS', 'Matt & Spot Laminatio'),
                      ('GL', 'Glossy Laminatio'),
                      ('GE', 'Glue Lamination'))
    coated_with = models.CharField('Coated with', max_length=2, choices = COATED_CHOICES )
    pages = models.IntegerField('Page / Book')
    cover_page_material = models.CharField('Cover Paper Material', max_length=100)
    cover_color_number = models.IntegerField('Cover Number of Printer Colors') # Restrict to 12 in validation
    body_page_material = models.CharField('Body Paper Material', max_length=100)
    number_pieces_master = models.IntegerField('Number of Pieces / Master')
    number_machine_master = models.IntegerField('Number of Machine / Master')
    machine_height = models.DecimalField('Machine Height (in inch)', max_digits = 3, decimal_places = 2)
    machine_width = models.DecimalField('Machine Width (in inch)', max_digits = 3, decimal_places = 2)
    MACHINE_CHOICES = (('GTO', 'GTO'),
                      ('GTO Big', 'GTO Big'),
                      ('Demai', 'Demai'),
                      ('Over Demai', 'Over Demai'),
                      ('Double Demai','Double Demai' ))
    machine_type = models.CharField('Machine Type', max_length=2, choices = COATED_CHOICES )
    weight = models.DecimalField('Weight (kilogram)', max_digits = 4, decimal_places = 2)
    base_quantity = models.IntegerField('Base Quantity')
    price_per_piece = models.DecimalField('Base Price per piece (BDT)', max_digits = 6, decimal_places = 2)
    increment_quantity = models.IntegerField('Increment Quantity')
    price_per_piece_increment = models.DecimalField('Increment per piece Price (rate after base quantity)', max_digits = 6, decimal_places = 2)

    def __str__(self):
        return self.name

class Quotation(models.Model):
    product = models.ManyToManyField(Product, through='QuotationProduct')
    shipping_charge = models.DecimalField('Shipping Charge', max_digits=20, decimal_places=2)
    vat_percent = models.DecimalField('Vat (Percent)', max_digits=5, decimal_places=2)
    tax_percent = models.DecimalField('Tax (Percent)', max_digits=5, decimal_places=2)
    advance_percent = models.DecimalField('Advance Payment (percent)', max_digits=5, decimal_places=2, default=50)
    #later_payment = models.DecimalField('To be paid later', max_digits=20, decimal_places= 2)
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)

    def get_quotation_price(self):
        """Sums prices of all product items. return total Quotation value"""
        price=0
        for item in self.quotationproduct_set.all():
            price = price + item.get_total_price()
        return price

    def get_advance_payment(self):
        advance = (self.get_quotation_price()*self.advance_percent)/100
        return advance

    def get_due_payment(self):
        due = self.get_quotation_price() - self.get_advance_payment()
        return due


class QuotationProduct(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quotation = models.ForeignKey(Quotation, on_delete= models.CASCADE)
    unit = models.IntegerField('Unit')
    price = models.DecimalField('Unit Price (BDT)', max_digits=20, decimal_places=2)

    def get_total_price(self):
        """ Calculates and returns price for a row"""
        price = self.unit * self.price
        return price
