import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='CSV file to import')

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            lte_exists_str = phone['lte_exists']
            boolean = True if lte_exists_str == "True" else False
            phone_name = Phone(
                id=int(phone['id']),
                name=str(phone['name']),
                image=str(phone['image']),
                price=float(phone['price']),
                release_date=str(phone['release_date']),
                lte_exists=boolean,
                slug=slugify(phone['name']),
            )
            phone_name.save()

