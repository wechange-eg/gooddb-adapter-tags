from django.conf import settings
import django
django.setup()

import csv

from core.models import Tag, Category

Tag.objects.all().delete()
Category.objects.all().delete()

with open('20190816_mapping.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=';')
    for row in csvReader:
        category, created = Category.objects.get_or_create(name=row[1])
        tag, created = Tag.objects.get_or_create(name=row[0], category=category)

