import mysql.connector
import streamlit as st
import pandas as pd

# Initialize connection.
# Uses st.cache to only run once.
@st.cache(allow_output_mutation=True, hash_funcs={'_thread.RLock' : lambda _: None, 'builtins.weakref': lambda _: None})
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

def read_from_database_streamlit(query, parse_dates, conn=None):
    df = pd.read_sql(query, conn, parse_dates=parse_dates)
    return df

