# mysqlinsert.py inserts data from given file into MySQL databse
# run: mysqlinsert.py -f filename to insert a file of tuples 
#      (col-0, col-1, col-2, ..., m)\n(col-0, col-1, col-2, ..., col-m)

from sys import argv
import csv

if __name__ == "__main__":
    if len(argv) < 2:
        usage("python3 mysqlinsert.py (file.csv)")
        exit();
    
    filename = argv[1]

    with open(filename) as csv_file: 
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print("insert row", row)
            
