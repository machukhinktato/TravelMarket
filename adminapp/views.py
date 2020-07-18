from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from mainapp.models import Accommodation
from mainapp.models import ListOfCountries
from authapp.models import ShopUser
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm
from adminapp.forms import AccommodationEditForm


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserRegisterForm()

    content = {
        'title': title,
        'update_form': user_form,
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {
        'title': title,
        'update_form': edit_form,
    }

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'

    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

        content = {
            'title': title,
            'update_form': user,
        }

        return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def countries(request):
    title = 'админка/страны'

    countries_list = ListOfCountries.objects.all()

    content = {
        'title': title,
        'objects': countries_list
    }

    return render(request, 'adminapp/countries.html', content)


@user_passes_test(lambda u: u.is_superuser)
def country_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def country_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def country_delete(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def accommodations(request, pk):
    title = 'админка/размещение'

    country = get_object_or_404(ListOfCountries, pk=pk)
    accommodation_list = Accommodation.objects.filter(country__id=pk).order_by('name')

    content = {
        'title': title,
        'country': country,
        'objects': accommodation_list,
    }

    return render(request, 'adminapp/accommodations.html', content)


@user_passes_test(lambda u: u.is_superuser)
def accommodation_create(request, pk):
    title = 'размещение/создание'
    country = get_object_or_404(ListOfCountries, pk=pk)
    if request.method  == 'POST':
        accommodation_form = AccommodationEditForm(request.POST, request.FILES)
        if accommodation_form.is_valid():
            accommodation_form.save()
            return HttpResponseRedirect(reverse('admin:accommodations', args=[pk]))
    else:
        accommodation_form = AccommodationEditForm(initial={'country': country})
    content = {
        'title':title,
        'update_form': accommodation_form,
        'country': country,
    }
    return render(request, 'adminapp/product_update.html')


@user_passes_test(lambda u: u.is_superuser)
def accommodation_read(request, pk):
    title = 'размещение/подробнее'
    accommodation = get_object_or_404(Accommodation, pk=pk)
    content = {
        'title': title,
        'accommodation': accommodation,
    }
    return render(request, 'adminapp/product_read.html', content)

@user_passes_test(lambda u: u.is_superuser)
def accommodation_update(request, pk):
    title = 'размещение/создание'
    country = get_object_or_404(ListOfCountries, pk=pk)
    if request.method == 'POST':
        accommodation_form = AccommodationEditForm(request.POST, request.FILES)
        if accommodation_form.is_valid():
            accommodation_form.save() #test cleaned_data
            return HttpResponseRedirect(reverse('admin:accommodations', args=[pk]))
    else:
        accommodation_form = AccommodationEditForm(initial={'country':country})
        content = {
            'title': title,
            'update_form': accommodation_form,
            'country': country,
        }
        return render(request, 'adminapp/accommodation_update.html', content)

@user_passes_test(lambda u: u.is_superuser)
def accommodation_delete(request, pk):
    title = 'размещение/удаление'

