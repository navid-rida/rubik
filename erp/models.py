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


