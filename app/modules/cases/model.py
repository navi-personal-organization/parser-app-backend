import psycopg2
import logging
import time
from app.credentials import postgresql_credentials as cred
from app.core import query_builder as query

logging.basicConfig(level=logging.INFO)


class CasesModel(object):

    @classmethod
    def insert_rows(cls, rows):
        con = psycopg2.connect(database=cred.database,
                               user=cred.user,
                               password=cred.password,
                               host=cred.host,
                               port=cred.port)
        cur = con.cursor()
        start_time = time.time()
        try:
            cur.execute(query.create_table())
            cur.executemany(query.insert_rows_query(), rows)
            con.commit()
        except Exception as e:
            logging.info(e)
        finally:
            cur.close()
            con.close()
            logging.info(('Elapsed time in saving: %s' % (time.time() - start_time)))

    @classmethod
    def get_top_confirmed(cls, obs_date, max_results):
        response = None
        con = psycopg2.connect(database=cred.database,
                               user=cred.user,
                               password=cred.password,
                               host=cred.host,
                               port=cred.port)
        cur = con.cursor()

        try:
            cur.execute(query.get_top_confirmed_query(), (obs_date, max_results))
            response = cur.fetchall()
        except Exception as e:
            logging.info(e)
        finally:
            cur.close()
            con.close()
        return response