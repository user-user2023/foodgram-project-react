import csv
import os

from django.core.management import BaseCommand

from recipes.models import Ingredient


CSV_FILES_DIR = os.path.dirname(os.path.dirname(os.getcwd()))


class Command(BaseCommand):
    help = 'Импорт ингредиентов из файла CSV.'

    def handle(self, *args, **kwargs):
        for row in csv.reader(open(
            f'{CSV_FILES_DIR}/foodgram-project-react/data/ingredients.csv',
            'r',
            encoding='utf-8'
        )):
            name = row[0]
            measurement_unit = row[1]
            ingredient, _ = Ingredient.objects.get_or_create(
                name=name,
                measurement_unit=measurement_unit
            )
            ingredient.save()
        self.stdout.write(
            self.style.SUCCESS('Ингредиенты успешно импортированны.')
        )


###from django.conf import settings

###CSV_FILES_DIR = settings.BASE_DIR

###import csv
####from django.conf import settings
####from backend.foodgram.foodgram.settings import BASE_DIR
###f'{CSV_FILES_DIR}/data/ingredients.csv'
###            os.path.join(CSV_FILES_DIR, 'data', 'ingredients.csv'),
###import os

###
###from django.conf import settings
###from django.core.management import BaseCommand
###from recipes.models import Ingredients
###
###
###
###CSV_FILES_DIR = settings.BASE_DIR
###
###
###class Command(BaseCommand):
###    def handle(self, *args, **kwargs):
###        for row in csv.reader(open(
###            f'{CSV_FILES_DIR}/ingredients.csv', 'r', encoding='utf-8'
###        )):
###            name = row['name'],
###            measurement_unit = row['measurement_unit'],
###            Ingredients.objects.get_or_create(
###                name=name,
###                measurement_unit=measurement_unit
###            )
###            Ingredients.save()

#from csv import DictReader

##import os
##from csv import DictReader
##
##from django.core.management import BaseCommand
##
##from backend.foodgram.recipes.models import Ingredients
###from backend.foodgram.foodgram.settings import BASE_DIR
###from foodgram.settings import BASE_DIR
##
###from foodgram.settings import BASE_DIR
##
###os.path.dirname(os.path.dirname(os.getcwd()))
##
###from recipes.models import Ingredients
##
###CSV_FILES_DIR = f"{BASE_DIR}../data/ingredients.csv"
##CSV_FILES_DIR = os.path.dirname(os.path.dirname(os.getcwd()))
##
##
##class Command(BaseCommand):
##    def handle(self, *args, **kwargs):
##        for row in DictReader(open(f'{CSV_FILES_DIR}/data/ingredients.csv')):
##            ingredients = Ingredients(
##                name=row['name'],
##                measurement_unit=row['measurement_unit'],
##            )
##            ingredients.save
##