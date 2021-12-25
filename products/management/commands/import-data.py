from csv import DictReader
import re
from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    # import data from ../data/tgdd.csv to product tables
    help = "Load data from tgdd.csv to product tables"

    def handle(self, *args, **options):
        with open('data/tgdd.csv', encoding='utf-8') as f:
            reader = DictReader(f)
            for row in reader:
                price = re.sub('\D', '', row['price'])
                Product.objects.create(
                    name=row['name'],
                    price=price,
                    image=row['image-src'],
                    description="lorem , ipsum ",
                    # brand=row['brand'],
                    # rating=row['rating'],
                )
