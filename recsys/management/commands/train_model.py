import re
from django.core.management.base import BaseCommand
from recsys.services import RecSysService, RecSysModel


class Command(BaseCommand):
    # import data from ../data/tgdd.csv to product tables
    help = "Export data from database to csv file and use surprise to train it"

    def handle(self, *args, **options):
        RecSysService.export_rating_to_csv()
        RecSysService.export_view_to_csv()

        model = RecSysModel.instance()
        model.train()
