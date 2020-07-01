from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/product.html')
