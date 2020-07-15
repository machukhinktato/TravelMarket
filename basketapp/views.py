from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
from mainapp.models import Accommodation


def basket(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(
        user=request.user).order_by('accommodation__country')

    content = {
        'title': title,
        'basket_items': basket_items,
    }

    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    accommodation = get_object_or_404(Accommodation, pk=pk)
    basket = Basket.objects.filter(user=request.user, accommodation=accommodation).first()

    if not basket:
        basket = Basket(user=request.user, accommodation=accommodation)

    basket.nights += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return render(request, 'basketapp/basket.html')
