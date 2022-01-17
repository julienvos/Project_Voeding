from mysql.connector import MySQLConnection, Error
from sqlalchemy.sql.functions import user
from python_mysql_dbconfig import read_db_config
import pandas as pd
from sqlalchemy import create_engine

def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')

def write_to_database(df, table_name):
    try:
        dbconfig = read_db_config()
        engine = create_engine('mysql+mysqlconnector://{user}:{password}@{host}:{port}/{dbname}'.format(host = dbconfig['host'],
                                                                                             user = dbconfig['user'],
                                                                                             password = dbconfig['password'],
                                                                                             port = dbconfig['port'],
                                                                                             dbname = dbconfig['database'] ))
        df.to_sql(table_name, engine)

    except Error as e:
        print(e)


def read_from_database(query, parse_dates=None):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        df = pd.read_sql(query, conn, parse_dates=parse_dates)


    except Error as e:
        print(e)

    finally:
        conn.close()
        return df






