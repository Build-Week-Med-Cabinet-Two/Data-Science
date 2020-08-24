import os
import psycopg2
import sqlite3
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "CanBase.db")
connection = sqlite3.connect(DB_FILEPATH)

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection_pg = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION_PG: ", type(connection_pg))
print("CONNECTION: ", type(connection))

cursor = connection.cursor()
cursor_pg = connection_pg.cursor()
print("CURSOR: ", type(cursor))
print("CURSOR_PG: ", type(cursor_pg))


## Create Cannabis Table in Postgres ##

create_cannabis_table_query = '''
CREATE TABLE IF NOT EXISTS cannabis (
    id SERIAL PRIMARY KEY,
      strain VARCHAR(30),
      type VARCHAR(30),
      rating INT,
      effects VARCHAR(30),
      flavor VARCHAR(30),
      description VARCHAR(30),
)
'''

add_data_query = '''
INSERT INTO cannabis (strain, trype, rating, effects, flavor, description) VALUES
(
    '13-Dawgs', 'hybrid', 4.2, 'Tingly, Creative',  'Apricot, Citrus', 'A hybrid of...'
)
'''

cursor_pg.execute(create_cannabis_table_query)
cursor_pg.execute(add_data_query)

entries = cursor.execute('SELECT * FROM cannabis').fetchall()

for entry in entries:

    insert_query = f''' INSERT INTO cannabis
        (id, strain, type, rating, effects, flavor, description) VALUES
        {entry}
    '''
    cursor_pg.execute(insert_query)

connection.commit()
connection.close()
connection_pg.commit()
connection_pg.close()
