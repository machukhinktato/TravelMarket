from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import ListOfCountries
from .models import Accommodation
from basketapp.models import Basket


def main(request):
    return render(request, 'mainapp/index.html')


def accommodations(request, pk=None):
    title = 'размещение'
    list_of_accommodations = Accommodation.objects.all()[:3]

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            accs = Accommodation.objects.all().order_by('price')
            country = {'name': 'все'}
        else:
            country = get_object_or_404(ListOfCountries, pk=pk)
            accs = Accommodation.objects.filter(
                country__pk=pk
            ).order_by('price')

        content = {
            'title': title,
            'list_of_accommodations': list_of_accommodations,
            'country': country,
            'accs': accs,
            'basket': basket,
        }
        return render(request, 'mainapp/accommodation_list.html', content)

    same_accs = Accommodation.objects.all()[3:5]

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
        'same_accs': same_accs,
        'basket': basket,
    }


    return render(request, 'mainapp/product.html', content)
