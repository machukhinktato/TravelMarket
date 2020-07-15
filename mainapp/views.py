from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
import random
from .models import ListOfCountries
from .models import Accommodation
from basketapp.models import Basket


def main(request):
    return render(request, 'mainapp/index.html')


def accommodations(request, pk=None):
    title = 'размещение'
    list_of_accommodations = Accommodation.objects.all()[:3]

    basket = get_basket(request.user)

    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            accommodations = Accommodation.objects.all().order_by('price')
            country = {'name': 'все'}
        else:
            country = get_object_or_404(ListOfCountries, pk=pk)
            accommodations = Accommodation.objects.filter(
                country__pk=pk
            ).order_by('price')

        content = {
            'title': title,
            'list_of_accommodations': list_of_accommodations,
            'country': country,
            'accommodations': accommodations,
            'basket': basket,
        }
        return render(request, 'mainapp/accommodation_list.html', content)

    hot_offer = get_hot_offer()
    same_accommodations = get_same_accommodations(hot_offer)

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
        'hot_offer': hot_offer,
        'same_accommodations': same_accommodations,
        'basket': basket,
    }

    return render(request, 'mainapp/accommodations.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_offer():
    accommodations = Accommodation.objects.all()

    return random.sample(list(accommodations), 1)[0]


def get_same_accommodations(hot_offers):
    same_offers = Accommodation.objects.filter(
        country=hot_offers.country).exclude(pk=hot_offers.pk)[:3]

    return same_offers
