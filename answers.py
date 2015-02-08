import eulermaths
import functools
import gmpy2
import math
import operator


def problem1():
    answer = []
    answer.extend(eulermaths.listMultiples(3, upperBound=1000))
    answer.extend(eulermaths.listMultiples(5, upperBound=1000))
    return sum(set(answer))


def problem2():
    answer = 0
    for i in range(2, 35):
        value = eulermaths.fibonacci(i)
        if (value % 2 == 0):
            answer += value
    return answer


def problem3():
    return max(eulermaths.listPrimeFactors(600851475143))


def problem4():
    answer = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            number = i*j
            if (str(number) == str(number)[::-1] and number > answer):
                answer = number
    return answer


def problem5():
    return int(functools.reduce(gmpy2.lcm, range(2, 21)))


def problem6():
    sumSquares = 0
    squareSum = 0
    for i in range(1, 101):
        sumSquares += math.pow(i, 2)
        squareSum += i
    squareSum = math.pow(squareSum, 2)
    return squareSum - sumSquares


def problem7():
    return eulermaths.nthPrime(10001)


def problem8():
    answer = 0
    digits = []
    with open('p8.txt', 'r') as number: # the file containing the 1000 digit number
        digits.extend(number.read())
        digits = list(map(int, digits)) # easiest to iterate over list of digits
    for i in range(0, 988):
        digitProduct = functools.reduce(operator.mul, digits[i:i+13])
        if (digitProduct > answer):
            answer = digitProduct
    return answer


def problem9():
    for a in range (1, 334):
        for b in range(i, 666):
            if (math.pow(a, 2) + math.pow(b, 2) == math.pow(1000-(a+b), 2)):
                # constraints: a+b+c = 1000, c = 1000-(a+b) and a^2 + b^2 = c^2
                return a*b*(1000-(a+b))


def problem10():
    answer = 0
    prime = 2
    while (prime < 2000000):
        answer += prime
        prime = int(gmpy2.next_prime(prime))
    return answer


def problem20():
    return sum([int(digit) for digit in str(math.factorial(100))])


def problem25():
    term = 0
    value = 0
    while (len(str(value)) < 1000):
        term += 1
        value = eulermaths.fibonacci(term)
    return term
