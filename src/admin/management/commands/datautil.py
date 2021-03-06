from os import path
import csv

from django.core.management import BaseCommand
from django.conf import settings
from django.db.models import Q

from user.models import Country, City, Major

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
        elif action == 'clearcountry':
            self.clear_country()
        elif action == 'seedmajor':
            self.seed_major()
        else:
            self.stdout.write('Cannot found action %s' % action)

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
        self.stdout.write('%s countries were seeded' % total)

        cities_data = path.join(DATA_DIR, 'cities.csv')
        total = 0
        with open(cities_data) as csv_file:
            cities = csv.reader(csv_file, delimiter='\t', quotechar='"')
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
        self.stdout.write('%s cities were seeded' % total)

        self.stdout.write('Done seeding country and city')


    def seed_major(self):
        majors_data = path.join(DATA_DIR, 'majors.csv')
        total = 0
        with open(majors_data) as csv_file:
            majors = csv.reader(csv_file, delimiter='\t', quotechar='"')
            for row in majors:
                params = dict({
                    'start_from': row[0],
                    'name': row[1],
                    'shorten': row[2],
                    'degree': row[3],
                })
                try:
                    major = Major.objects.get(shorten=row[2])
                except Major.DoesNotExist:
                    major = Major.objects.create(**params)
                    major.save()
                    total += 1
        self.stdout.write('%s majors were seeded' % total)


        self.stdout.write('Done seeding major and intake')

    def clear_country(self):
        countries = Country.objects.all()
        for c in countries:
            c.delete()

        self.stdout.write('Done clearing %s countries' % len(countries))
