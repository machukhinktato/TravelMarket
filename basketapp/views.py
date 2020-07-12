from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
from mainapp.models import Accommodation


def basket(request):
    content = {}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    accommodation = get_object_or_404(Accommodation, pk=pk)
    basket = Basket.objects.filter(user=request.user, accommodation=accommodation).first()

    if not basket:
        basket = Basket(user=request.user, accommodation=accommodation)

    basket.staying += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    content = {}
    return render(request, 'basketapp/basket.html', content)