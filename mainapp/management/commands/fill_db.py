from django.core.management.base import BaseCommand
from mainapp.models import ListOfCountries, Accommodation
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='cp-1252') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        countries = load_from_json('countries')

        ListOfCountries.objects.all().delete()
        for country in countries:
            new_country = ListOfCountries(**country)
            new_country.save()

        accommodations = load_from_json('accommodations')

        Accommodation.objects.all().delete()
        for acc in accommodations:
            acc_location = acc["country"]
            _country = ListOfCountries.objects.get(name=acc_location)
            acc['country'] = _country
            new_acc = Accommodation(**acc)
            new_acc.save()

    super_user = User.objects.create_superuser('tarab', 'tarab@mail.ru', 'geekbrains')