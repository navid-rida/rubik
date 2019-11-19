from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
@login_required
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    context = {'testdata': "This is just for testing"}
    return render(request, 'erp/blank-page-header.html', context)
