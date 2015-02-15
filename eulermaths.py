from gmpy2 import is_prime, next_prime
from functools import lru_cache, reduce
from operator import mul


def list_multiples(multiple=1, lowerBound=0, upperBound=1000000):
    return [i for i in range(lowerBound, upperBound, multiple)]


lru_cache(maxsize=128)
def fibonacci(number):
    if (number == 0):
        return 0
    elif (number <= 2):
        return 1
    return fibonacci(number-1) + fibonacci(number-2)


def list_factors(number):
    factors = [number]
    for i in range(2, int(number**0.5)+1):
        if (number % i == 0):
            factors.append(i)
            factors.append(int(number/i))
    return factors


def list_prime_factors(number):
    return [i for i in list_factors(number) if is_prime(i)]


def nth_prime(n):
    numberOfPrime = 1
    result = 2
    while (n > numberOfPrime):
        result = next_prime(result)
        numberOfPrime += 1
    return int(result)


def sum_factors(number):
    return 1 + sum(list_factors(number)) - number


def is_amicable(number):
    return sum_factors(sum_factors(number)) == number and sum_factors(number) != number


def number_spiral(dimension):
    if (dimension == 1):
        return 1
    return 4*dimension**2 - 6*(dimension-1) + number_spiral(dimension-2)

    
def letter_value(letter):
    return ord(letter.upper()) - 64


def word_value(word):
    wordValue = 0
    for letter in word.upper():
        wordValue += letter_value(letter)
    return wordValue

    
lru_cache(maxsize=128)
def lattice_paths(row, column):
    if (row == 0 or column == 0):
        return 1
    return lattice_paths(row-1, column) + lattice_paths(row, column-1)


def largest_product(grid):
    products = []
    gridT = list(map(list, zip(*grid)))
    for i in range(0, 4):
        products.append(reduce(mul, grid[i]))
        products.append(reduce(mul, gridT[i]))
    products.append(grid[0][0]*grid[1][1]*grid[2][2]*grid[3][3])
    products.append(grid[3][0]*grid[2][1]*grid[1][2]*grid[0][3])
    return max(products)


collatz_cache = {1:1}
lru_cache(maxsize=128)
def collatz_length(number):
    if (number not in collatz_cache):
        if (number % 2 == 0):
            collatz_cache[number] = 1 + collatz_length(number/2)
        else:
            collatz_cache[number] = 1 + collatz_length(3*number + 1)
    return collatz_cache[number]
