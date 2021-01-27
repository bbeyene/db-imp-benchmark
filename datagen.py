# datagen.py generates data following spec of the Wisconsin Benchmark Paper

"""
Attribute-Name | Range-of-Values | Order | Comment
unique1 0-(MAXTUPLES-1) random unique, random order
unique2 0-(MAXTUPLES-1) sequential unique, sequential
two 0-1 random (unique1 mod 2)
four 0-3 random (unique1 mod 4)
ten 0-9 random (unique1 mod 10)
twenty 0-19 random (unique1 mod 20
onePercent 0-99 random (unique1 mod 100)
tenPercent 0-9 random (unique1 mod 10)
twentyPercent 0-4 random (unique1 mod 5)
fiftyPercent 0-1 random (unique1 mod 2)
unique3 0-(MAXTUPLES-1) random unique1
evenOnePercent 0,2,4,...,198 random (onePercent * 2)
oddOnePercent 1,3,5,...,199 random (onePercent * 2)+1
stringu1 - random candidate key
stringu2 - random candidate key
string4 - cyclic
"""

if __name__ == "__main__":
    print("nothing yet")
