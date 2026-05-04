import pandas as pd
import sqlite3
import os

DB_PATH = "data_store/market_data.db"


def get_connection():
    os.makedirs("data_store", exist_ok=True)
    return sqlite3.connect(DB_PATH)


def save_data(df: pd.DataFrame, table_name="market_data"):
    conn = get_connection()
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()


def load_data(table_name="market_data"):
    conn = get_connection()
    try:
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
        conn.close()
        return df
    except:
        conn.close()
        return None