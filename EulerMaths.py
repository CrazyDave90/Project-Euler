import gmpy2
import math
fibCache = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34}


def listMultiples(multiple=1, lowerBound=0, upperBound=math.pow(10, 6)):
    return [n for n in range(lowerBound, upperBound, multiple)]


def fibonacci(number):
    while (number not in fibCache):
            fibCache[len(fibCache)+1] = fibCache[len(fibCache)] + fibCache[len(fibCache)-1]
    return fibCache[number]


def listFactors(number):
    factors = [number]
    for n in range(2, int(math.sqrt(number))+1):
        if (number % n == 0):
            factors.append(n)
            factors.append(int(number/n))
    return factors


def isPrime(number):
    return gmpy2.is_prime(number)


def listPrimeFactors(number):
    return [n for n in listFactors(number) if isPrime(n)]


def nthPrime(n):
    numberOfPrime = 1
    result = 2
    while n > numberOfPrime:
        result = gmpy2.next_prime(result)
        numberOfPrime += 1
    return int(result)


def greatestCommonFactor(a, b):
    return int(gmpy2.gcd(a, b))


def leastCommonMultiple(a, b):
    return int(gmpy2.lcm(a, b))

