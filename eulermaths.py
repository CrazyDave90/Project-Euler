import gmpy2
import math


fibCache = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34}


def listMultiples(multiple=1, lowerBound=0, upperBound=10**6):
    return [i for i in range(lowerBound, upperBound, multiple)]


def fibonacci(number):
    while (number not in fibCache):
            fibCache[len(fibCache)] = fibCache[len(fibCache)-1] + fibCache[len(fibCache)-2]
    return fibCache[number]


def listFactors(number):
    factors = [number]
    for i in range(2, int(number**0.5)+1):
        if (number % i == 0):
            factors.append(i)
            factors.append(int(number/i))
    return factors


def listPrimeFactors(number):
    return [i for i in listFactors(number) if gmpy2.is_prime(i)]


def nthPrime(n):
    numberOfPrime = 1
    result = 2
    while (n > numberOfPrime):
        result = gmpy2.next_prime(result)
        numberOfPrime += 1
    return int(result)


def sumFactors(number):
    return 1 + sum(listFactors(number)) - number


def isAmicable(number):
    return sumFactors(sumFactors(number)) == number and sumFactors(number) != number
