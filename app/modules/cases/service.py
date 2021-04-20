import csv
import logging
import time
from multiprocessing import Process
from more_itertools import chunked
from datetime import datetime
from model import CasesModel as model
from app.core import service_util

logging.basicConfig(level=logging.INFO)


class CasesService(object):
    file_name = 'data/covid_19_data.csv'
    chuck_size = 5000

    @classmethod
    def parse_csv(cls):
        start_time = time.time()
        with open(cls.file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)

            # chunked_data = chunked(csv_reader, cls.chuck_size)
            # for row in chunked_data:
            #     p = Process(target=cls.process_data, args=[row])
            #     p.start()
            #     p.join()

            cls._process_data(csv_reader)

        logging.info(('Total elapsed time processing: %s' % (time.time() - start_time)))

    @classmethod
    def _process_data(cls, chunked_data):
        rows = []
        start_time = time.time()
        for row in chunked_data:
            obj = [
                service_util.clean_num(row[0]),
                service_util.clean_date(row[1]),
                row[2],
                row[3],
                service_util.clean_date_time(row[4]),
                service_util.clean_num(row[5]),
                service_util.clean_num(row[6]),
                service_util.clean_num(row[7])
            ]
            rows.append(obj)
        logging.info(('Elapsed time in parsing: %s' % (time.time() - start_time)))
        model.insert_rows(rows)

    @classmethod
    def get_top_confirmed(cls, obs_date, max_results):
        date_param = datetime.strptime(obs_date, '%Y-%m-%d').date()
        num_param = int(max_results)
        result = model.get_top_confirmed(date_param, num_param)
        return service_util.build_response(obs_date, result)