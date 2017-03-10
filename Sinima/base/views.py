from django.shortcuts import render
from django.views.generic import DeleteView,ListView
# Create your views here.

def index(request):
    return render(request, template_name='base/home.html')
def contact(request):
    return render(request, template_name='base/contact.html')