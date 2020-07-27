from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Q
import random
from .models import ListOfCountries
from .models import Regions
from .models import Accommodation
from basketapp.models import Basket
# from . import context_processors


def main(request):
    return render(request, 'mainapp/index.html')


def accommodation(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ListOfCountries.objects.all(),
        'accommodation': get_object_or_404(Accommodation, pk=pk),
    }

    return render(request, 'mainapp/accommodation_details.html', content)


def accommodations(request, pk=None, page=1):
    title = 'размещение'

    list_of_accommodations = Accommodation.objects.filter(is_active=True)

    if pk is not None:
        if pk == 0:
            country = {'pk': 0, 'name': 'все'}
            accommodations = Accommodation.objects.filter(
                is_active=True, country__is_active=True
            ).order_by('price')
        else:
            country = get_object_or_404(ListOfCountries, pk=pk)
            accommodations = Accommodation.objects.filter(
                country__pk=pk, is_active=True, country__is_active=True
            ).order_by('price')

        paginator = Paginator(accommodations, 2)
        try:
            accommodations_paginator = paginator.page(page)
        except PageNotAnInteger:
            accommodations_paginator = paginator.page(1)
        except EmptyPage:
            accommodations_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'list_of_accommodations': list_of_accommodations,
            'country': country,
            'accommodations': accommodations_paginator,
            # 'basket': basket,
        }
        return render(request, 'mainapp/accommodation_list.html', content)

    hot_offer = get_hot_offer()
    same_accommodations = get_same_accommodations(hot_offer)

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
        'hot_offer': hot_offer,
        'same_accommodations': same_accommodations,
        # 'basket': basket,
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
