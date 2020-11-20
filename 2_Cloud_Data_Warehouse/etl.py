import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Load data from the logs to the staging tables
    :param cur: The cursor of the connection
    :param conn: The connection itself
    :return:None
    """
    for query in copy_table_queries:
        print("executing load_staging_tables")
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Insert data from the staging tables to the analytical tables
    :param cur: The cursor of the connection
    :param conn: The connection itself
    :return:None
    """
    for query in insert_table_queries:
        print("executing insert_tables")
        cur.execute(query)
        conn.commit()


def main():
    print("Executing main")
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()