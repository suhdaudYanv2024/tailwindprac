from django.shortcuts import render
# http response
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'tailwindprac/home.html')
