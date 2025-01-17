import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    for query in drop_table_queries:
        print('Executing drop query : ' + query)
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        print('Executing create table : ' + query)
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    print('Connecting to Redshift')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    print('Redshift Connected')

    cur = conn.cursor()

    print('Dropping any tables if any')
    drop_tables(cur, conn)

    create_tables(cur, conn)
    print('Tables Created')

    conn.close()


if __name__ == "__main__":
    main()
