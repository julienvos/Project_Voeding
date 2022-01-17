#connect to database
import mysql.connector
from mysql.connector import Error


# function to connect to database and get the table data (can also be in a seperate .py file and be called with an import )
def get_data(query=None, date_col=None):
    """ Connect to MySQL database
    exit()
    query is of datatype String
    
    """


    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       port=3306,
                                       database='voeding_database',
                                       user='root',
                                       password='root')
        if conn.is_connected():
            print('Connected to MySQL database')
            
        df = pd.read_sql(query, conn, parse_dates=date_col)
        return df

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

