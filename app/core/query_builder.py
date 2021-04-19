
def insert_rows_query():
    return """INSERT INTO covid_observations(sno,observation_date,province_state,country_region,
        last_update,confirmed,deaths,recovered) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""


def create_table():
    return """CREATE TABLE IF NOT EXISTS covid_observations(
           id SERIAL PRIMARY KEY,
           sno INTEGER,
           observation_date DATE,
           province_state VARCHAR(100),
           country_region VARCHAR(100),
           last_update TIMESTAMP,
           confirmed INTEGER,
           deaths INTEGER,
           recovered INTEGER)"""


def get_top_confirmed_query():
    return """SELECT country_region, confirmed, deaths, recovered
                FROM covid_observations
                WHERE observation_date = %s
                ORDER BY confirmed DESC
                LIMIT %s"""