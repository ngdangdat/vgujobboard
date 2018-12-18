from os import path
import csv

from django.core.management import BaseCommand
from django.conf import settings
from django.db.models import Q

from user.models.profile import Country, City

BASE_DIR = settings.BASE_DIR
DATA_DIR = path.join(BASE_DIR, 'data')

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('action', nargs='?',
                            help='Action of datautil')

    def handle(self, **options):
        action = options.pop('action')

        if not action:
            self.stdout.write('Please provide an action')

        # Seed country, city and major, intake
        if action == 'seedcountry':
            self.seed_country()

    def seed_country(self):
        countries_data = path.join(DATA_DIR, 'countries.csv')
        with open(countries_data) as csv_file:
            countries = csv.reader(csv_file, delimiter='\t', quotechar='"')
            total = 0
            for row in countries:
                country_id = row[0]
                country_name = row[1]
                try:
                    country = Country.objects.get(Q(id=country_id), Q(name=country_name))
                except Country.DoesNotExist:
                    # Create if country does not exist
                    country = Country.objects.create(id=country_id, name=country_name)
                    country.save()
                    total += 1
        self.stdout.write('%s countries was seeded' % total)

        cities_data = path.join(DATA_DIR, 'cities.csv')
        with open(cities_data) as csv_file:
            cities = csv.reader(csv_file, delimiter='\t', quotechar='"')
            total = 0
            for row in cities:
                city_id = row[0]
                city_name = row[1]
                country_id = row[2]
                try:
                    city = City.objects.get(id=city_id)
                except City.DoesNotExist:
                    # Create if city doesn't exist
                    city = City.objects.create(id=city_id, name=city_name, country_id=country_id)
                    city.save()
                    total += 1
        self.stdout.write('%s cities was seeded' % total)

        self.stdout.write('Done seeding country and city')


    def seed_major(self):
        self.stdout.write('Done seeding major and intake')
