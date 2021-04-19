import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)


def clean_date_time(data):

    try:
        processed_date = data.replace('/', '-')
        processed_date = processed_date.replace('T', ' ')
        date_arr = processed_date.split(' ')

        date = date_arr[0].split('-')
        time = date_arr[1].split(':')

        month = int(date[0])
        day = int(date[1])
        year = int(date[2])

        if len(date[0]) > 2:
            month = int(date[1])
            day = int(date[2])
            year = int(date[0])

        hour = int(time[0])
        minute = int(time[1])

        if len(time) == 3:
            second = int(time[2])
        else:
            second = 0

        return datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
    except Exception as e:
        logging.info(e)
        return None


def clean_date(data):

    try:
        processed_date = data.replace('/', '-')
        date_arr = processed_date.split('-')

        month = int(date_arr[0])
        day = int(date_arr[1])
        year = int(date_arr[2])

        if len(date_arr[0]) > 2:
            month = int(date_arr[1])
            day = int(date_arr[2])
            year = int(date_arr[0])

        return datetime(year=year, month=month, day=day).date()
    except Exception as e:
        logging.info(e)
        return None


def clean_num(data):
    return int(float(data))


def build_response(obs_date, result):
    obj_arr = []
    for row in result:
        obj = {
            'country': row[0],
            'confirmed': row[1],
            'deaths': row[2],
            'recovered': row[3]
        }
        obj_arr.append(obj)

    return {
        'observation_date': obs_date,
        'countries': obj_arr
    }
