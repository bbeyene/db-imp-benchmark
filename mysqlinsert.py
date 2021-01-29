# mysqlinsert.py inserts data from given file into MySQL databse
# run: mysqlinsert.py (file) to insert a csv file of tuples 
# https://realpython.com/python-mysql/

from sys import argv
import csv
from getpass import getpass
from mysql.connector import connect, Error

def create_database(connection):
    with connection.cursor() as cursor:
        create_db_query = "CREATE DATABASE Benchmark_Data"
        cursor.execute(create_db_query)
        use_db_query = "USE Benchmark_Data"
        cursor.execute(use_db_query)
        connection.commit()

def create_table(connection):
    with connection.cursor() as cursor:
        create_table_query = """
        CREATE TABLE ONEKTUP (
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


if __name__ == "__main__":
    if len(argv) < 2:
        usage("python3 mysqlinsert.py (file.csv)")
        exit();
    
    filename = argv[1]

    # https://realpython.com/python-mysql/
    try:
        with connect(
            host='see gcp sql instance ip',
            user='root',
            password=getpass("password: "),
        ) as connection:
            create_database(connection)
            create_table(connection)
    except Error as e:
        print(e)


    with open(filename) as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print("insert row", row)
            
