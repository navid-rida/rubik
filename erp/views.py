from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.generic.edit import CreateView
from .models import Customer


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
    fields=['name',]