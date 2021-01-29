# datagen.py generates data following spec of the Wisconsin Benchmark Paper
# run: datagen.py -m 10000 to generate a TENKTUP

from sys import argv
import random
import copy

if __name__ == "__main__":
    if len(argv) < 2:
        usage("python3 datagen.py (MAXTUPLES)")
        exit();

    MAX = int(argv[1])

    # unique2 0-(MAXTUPLES-1) sequential unique, sequential
    unique2 = range(MAX)

    # unique1 0-(MAXTUPLES-1) random unique, random order
    unique1 = random.sample(unique2, MAX)

    # two 0-1 random (unique1 mod 2)
    two = list(u1 % 2 for u1 in unique1)

    # four 0-3 random (unique1 mod 4)
    four = list(u1 % 4 for u1 in unique1)

    # ten 0-9 random (unique1 mod 10)
    ten = list(u1 % 10 for u1 in unique1)

    # twenty 0-19 random (unique1 mod 20
    twenty = list(u1 % 20 for u1 in unique1)

    # onePercent 0-99 random (unique1 mod 100)
    onePercent = list(u1 % 100 for u1 in unique1)

    # tenPercent 0-9 random (unique1 mod 10)
    tenPercent = list(u1 % 10 for u1 in unique1)

    # twentyPercent 0-4 random (unique1 mod 5)
    twentyPercent = list(u1 % 5 for u1 in unique1)

    # fiftyPercent 0-1 random (unique1 mod 2)
    fiftyPercent = list(u1 % 2 for u1 in unique1)

    # unique3 0-(MAXTUPLES-1) random unique1
    unique3 = copy.deepcopy(unique1)

    # evenOnePercent 0,2,4,...,198 random (onePercent * 2)
    evenOnePercent = list(2 * one for one in onePercent)

    # oddOnePercent 1,3,5,...,199 random (onePercent * 2)+1
    oddOnePercent = list(2 * one + 1 for one in onePercent)

    # TODO stringu1 - random candidate key
    # TODO stringu2 - random candidate key
    # TODO string4 - cyclic

    # TODO add stringu1, stringu2, string4 to zip
    tuples = list(zip(unique1, unique2, two, four, ten, twenty, onePercent, tenPercent, twentyPercent, fiftyPercent, unique3, evenOnePercent, oddOnePercent))
    print("unique1,unique2,two,four,ten,twenty,onePercent,tenPercent,twentyPercent,fiftyPercent,unique3,evenOnePercent,oddOnePercent")
    for tup in tuples:
        print(*tup, sep=',')
