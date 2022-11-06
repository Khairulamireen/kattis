from math import sqrt


def isPrime(value):
    i = 2
    primey = True
    while i <= sqrt(value):
        if (value % i == 0):
            primey = False

        i+=1
    
    return print(primey)

isPrime(4)