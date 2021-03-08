from multiprocessing import Process
from mysql.connector import connect, Error
from time import time

def read_then_write(db):
    print('read_then_write: starting')
    try:
        with connect(host='localhost', user='root', password='implementation') as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT count(*) FROM {db}.ONEMTUP WHERE tenPercent = 0;")
                result = cursor.fetchall()
                cursor.execute(f"UPDATE {db}.ONEMTUP SET string4 = 'x' where tenPercent = 0")
                result = cursor.fetchall()
                print(result)
    except Error as e: print(e)
    print('read_then_write: finishing')

def write_then_read(db):
    print('write_then_read: starting')
    try:
        with connect(host='localhost', user='root', password='implementation') as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"UPDATE {db}.ONEMTUP SET string4 = 'x' where tenPercent = 0")
                result = cursor.fetchall()
                cursor.execute(f"SELECT count(*) FROM {db}.ONEMTUP WHERE tenPercent = 0;")
                result = cursor.fetchall()
                print(result)
    except Error as e: print(e)
    print('write_then_read: finishing')

if __name__ == '__main__':
    # https://stackoverflow.com/questions/7207309/how-to-run-functions-in-parallel
    def runInParallel(*fns):
        proc = []
        for fn in fns:
            p = Process(target=fn)
            p.start()
            proc.append(p)
        for p in proc:
            p.join()

    tic = time()
    runInParallel(read_then_write('innoDB'), write_then_read('innoDB'), 
                    write_then_read('innoDB'), read_then_write('innoDB'), 
                    read_then_write('innoDB'), write_then_read('innoDB'), 
                    write_then_read('innoDB'), read_then_write('innoDB'))
    toc = time()
    print('4 concurrent InnoDB R/W: ', toc - tic)

    tic = time()
    runInParallel(read_then_write('myisam'), write_then_read('myisam'), 
                    write_then_read('myisam'), read_then_write('myisam'), 
                    read_then_write('myisam'), write_then_read('myisam'), 
                    write_then_read('myisam'), read_then_write('myisam'))
    toc = time()
    print('4 concurrent MyISAM R/W: ', toc - tic)