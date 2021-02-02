# mysqlinsert.py creates databases and tables, 
#                inserts csv from given file into MySQL database
#
# replace host = <instance-ip>
# run: mysqlinsert.py (file)
#
# https://realpython.com/python-mysql/

from sys import argv
import csv
from getpass import getpass
from mysql.connector import connect, Error

def create_database(name, connection):
    with connection.cursor() as cursor:
        create_db_query = f"CREATE DATABASE {name}"
        cursor.execute(create_db_query)
        use_db_query = f"USE {name}"
        cursor.execute(use_db_query)
        connection.commit()

def use_database(name, connection):
    with connection.cursor() as cursor:
        use_db_query = f"USE {name}"
        cursor.execute(use_db_query)

def create_table(name, connection):
    with connection.cursor() as cursor:
        create_table_query = f"""
        CREATE TABLE {name} (
        unique1 INT NOT NULL,
        unique2 INT PRIMARY KEY,
        two INT NOT NULL,
        four INT NOT NULL,
        ten INT NOT NULL,
        twenty INT NOT NULL,
        onePercent INT NOT NULL,
        tenPercent INT NOT NULL,
        twentyPercent INT NOT NULL,
        fiftyPercent INT NOT NULL,
        unique3 INT NOT NULL,
        evenOnePercent INT NOT NULL,
        oddOnePercent INT NOT NULL,
        stringu1 CHAR(52) NOT NULL,
        stringu2 CHAR(52) NOT NULL,
        string4 CHAR(52) NOT NULL
        ) """
        cursor.execute(create_table_query)
        connection.commit()

def insert_csv(table, filename, connection):
    with connection.cursor() as cursor:
        with open(filename) as csv_file:
            csv_data = csv.reader(csv_file)
            list_data = []
            for row in csv_data:
                list_data.append(tuple(row))

            query = f"INSERT INTO {table}(unique1,unique2,two,four,ten,twenty,onePercent,tenPercent,twentyPercent,fiftyPercent,\
                    unique3,evenOnePercent,oddOnePercent,stringu1,stringu2,string4) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cursor.executemany(query, list_data)
            connection.commit()

if __name__ == "__main__":
    if len(argv) < 2:
        usage("python3 mysqlinsert.py (file.csv)")
        exit();
    
    filename = argv[1]

    # https://realpython.com/python-mysql/
    try:
        with connect(
            host='', # gcp sql instance ip
            user='root',
            password=getpass("password: "),
        ) as connection:
            create_database('Benchmark_Data', connection)
            use_database('Benchmark_Data', connection)
            create_table('ONEKTUP', connection)
            insert_csv('ONEKTUP', filename, connection)
    except Error as e:
        print(e)


