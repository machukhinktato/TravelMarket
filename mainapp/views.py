from django.shortcuts import render
from django.http import HttpResponse
from .models import ListOfCountries, Accommodation


def main(request):
    return render(request, 'mainapp/index.html')


def accommodations(request):
    title = 'размещение'

    accommodations = Accommodation.objects.all()[:3]

    content = {'title': title, 'accommodations': accommodations}
    return render(request, 'mainapp/product.html', context=content)
