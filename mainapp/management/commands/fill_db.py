from django.core.management.base import BaseCommand
from mainapp.models import ListOfCountries
from mainapp.models import Accommodation
from mainapp.models import Regions
from django.contrib.auth.models import User
from authapp.models import ShopUser

import json, os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        countries = load_from_json('countries')

        ListOfCountries.objects.all().delete()
        for country in countries:
            new_country = ListOfCountries(**country)
            new_country.save()

        regions = load_from_json('regions')

        Regions.objects.all().delete()
        for _region in regions:
            region_location = _region["country"]
            _country = ListOfCountries.objects.get(name=region_location)
            _region["country"] = _country
            new_region = Regions(**_region)
            new_region.save()

        accommodations = load_from_json('accommodations')

        Accommodation.objects.all().delete()
        for acc in accommodations:
            acc_location = acc["country"]
            _country = ListOfCountries.objects.get(name=acc_location)
            acc['country'] = _country
            acc_region = acc["region"]
            acc_reg = Regions.objects.get(name=acc_region)
            acc['region'] = acc_reg
            new_acc = Accommodation(**acc)
            new_acc.save()

    super_user = ShopUser.objects.create_superuser('tarab', 'tarab@mail.ru', 'geekbrains')