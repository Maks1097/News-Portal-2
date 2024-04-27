from django.core.management.base import BaseCommand, CommandError
from simpleapp.models import New, Category


class Command(BaseCommand):
    help = 'Удаляет все новости.'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы действительно хотите удалить все новости в категории {options["category"]}? да/нет')

        if answer != 'yes':
            New.objects.all().delete()
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            New.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Все новости в категории {category.name} удалены.'))
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Не удалось найти категорию {category.name}'))