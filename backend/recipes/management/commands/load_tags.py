from django.core.management import BaseCommand
from recipes.models import Tags


class Command(BaseCommand):
    help = 'Загрузка tags.'

    def handle(self, *args, **kwargs):
        data = [
            {'name': 'Завтрак', 'color': '#e26c2d', 'slug': 'breakfast'},
            {'name': 'Обед', 'color': '#e22d49', 'slug': 'lunch'},
            {'name': 'Ужин', 'color': '#ab182e', 'slug': 'dinner'},
        ]
        for tags in data:
            Tags.objects.create(**tags)
        self.stdout.write(self.style.SUCCESS('Загрузка Tags завершена.'))
