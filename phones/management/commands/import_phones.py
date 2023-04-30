import csv
import re

from django.core.management.base import BaseCommand
from main.settings import PHONES_CSV
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(PHONES_CSV) as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone = Phone(
                name=phone['name'],
                image=phone['image'],
                price=phone['price'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=(re.sub(r'\s', '-', phone['name'])).lower()
            )
            phone.save()