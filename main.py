import sys

import psycopg2
import os
from dotenv import load_dotenv


def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST"),
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            port=os.getenv("POSTGRE_PORT"),
        )
        print("Successfully connected with the database")
        cur = conn.cursor()
        cur.execute('SELECT version()')
        print(cur.fetchone())
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("failed to connect with the database", error)
    finally:
        if conn is not None:
            print("Closed connection with the database")
            conn.close()


def main(argv):
    if len(argv) != 1:
        raise Exception("invalid/nil cmd line argument")
    if argv[0] == "dev":
        load_dotenv()
    connect()


if __name__ == "__main__":
    main(sys.argv[1:])
