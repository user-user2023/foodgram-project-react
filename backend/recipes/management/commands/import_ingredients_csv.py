import csv
import os
from django.core.management import BaseCommand

from recipes.models import Ingredient

CSV_FILES_DIR = os.path.dirname(os.path.dirname(os.getcwd()))


class Command(BaseCommand):
    help = 'Импорт ингредиентов из файла CSV.'

    def handle(self, *args, **kwargs):
        for row in csv.reader(open(
            f'{CSV_FILES_DIR}data/ingredients.csv',
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
