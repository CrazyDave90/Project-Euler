import math
fibCache = {1:0, 2:1, 3:1, 4:2, 5:3, 6:5, 7:8, 8:13, 9:21, 10:34}


def listMultiples(multiple=1, lowerBound=0, upperBound=10**6):
    return [n for n in range(lowerBound, upperBound, multiple)]


def fibonacci(number):
    while (number not in fibCache):
            fibCache[len(fibCache)+1] = fibCache[len(fibCache)] + fibCache[len(fibCache)-1]
    return fibCache[number]


def listFactors(number):
    factors = [1, number]
    for n in range(2, int(math.sqrt(number)) + 1):
        if (number % n == 0):
            factors.append(n)
            factors.append(number/n)
    return factors


def isPrime(number):
    if (len(listFactors(number)) > 2):
        return False
    return True


def listPrimeFactors(number):
    return [n for n in listFactors(number) if isPrime(n)]
