import csv
from tqdm import tqdm
import logging

from django.core.management.base import BaseCommand
from core.models import Policeorders

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "csv_record.log",
                    filemode = "w",
                    format = LOG_FORMAT,
                    level = logging.INFO)

logger = logging.getLogger()

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csv_file in options['csv_file']:
            order_count = 0
            with open(csv_file) as csv_progress:
                lines = len(csv_progress.readlines())
            dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')
            next(dataReader, None)
            for row in tqdm(dataReader, total=lines):
                order = Policeorders()
                order.crimeid = int(row[0])
                order.originalcrimetypename = row[1]
                order.reportdate = row[2]
                order.calldate = row[3]
                order.offensedate = row[4]
                order.calltime = row[5]
                order.calldatetime = row[6]
                order.disposition = row[7]
                order.address = row[8]
                order.city = row[9]
                order.state = row[10]
                order.agencyid = int(row[11])
                order.addresstype = row[12]
                order.commonlocation = row[12]

                order.save()
                order_count += 1
                logger.info(f'Order {order.address} - {order.reportdate} was recorded')

            self.stdout.write(f'Number of orders {order_count}')