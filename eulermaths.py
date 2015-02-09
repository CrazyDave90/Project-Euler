import gmpy2
import math


fibCache = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34}


def list_multiples(multiple=1, lowerBound=0, upperBound=1000000):
    return [i for i in range(lowerBound, upperBound, multiple)]


def fibonacci(number):
    while (number not in fibCache):
            fibCache[len(fibCache)] = fibCache[len(fibCache)-1] + fibCache[len(fibCache)-2]
    return fibCache[number]


def list_factors(number):
    factors = [number]
    for i in range(2, int(number**0.5)+1):
        if (number % i == 0):
            factors.append(i)
            factors.append(int(number/i))
    return factors


def list_prime_factors(number):
    return [i for i in list_factors(number) if gmpy2.is_prime(i)]


def nth_prime(n):
    numberOfPrime = 1
    result = 2
    while (n > numberOfPrime):
        result = gmpy2.next_prime(result)
        numberOfPrime += 1
    return int(result)


def sum_factors(number):
    return 1 + sum(list_factors(number)) - number


def is_amicable(number):
    return sum_factors(sum_factors(number)) == number and sum_factors(number) != number


def letter_value(letter):
    return ord(letter.upper()) - 64


def word_value(word):
    wordValue = 0
    for letter in word.upper():
        wordValue += letter_value(letter)
    return wordValue
    
