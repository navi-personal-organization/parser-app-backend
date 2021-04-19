import csv
import logging
from datetime import datetime
from model import CasesModel as model
from app.core import service_util

logging.basicConfig(level=logging.INFO)


class CasesService(object):
    file_name = 'data/covid_19_data.csv'

    @classmethod
    def parse_csv(cls):
        rows = []
        with open(cls.file_name) as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for row in csv_reader:
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
        model.insert_rows(rows)

    @classmethod
    def get_top_confirmed(cls, obs_date, max_results):
        date_param = datetime.strptime(obs_date, '%Y-%m-%d').date()
        num_param = int(max_results)
        result = model.get_top_confirmed(date_param, num_param)
        return service_util.build_response(obs_date, result)