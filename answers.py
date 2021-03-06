from eulermaths import *
from gmpy2 import is_prime, next_prime, lcm
from math import factorial, log10
from operator import mul
from functools import reduce
from num2words import num2words
from itertools import count, permutations, combinations, islice, product
from calendar import weekday
from fractions import Fraction


def problem1():
    return sum([n for n in range(1000) if n % 3 == 0 or n % 5 == 0])


def problem2():
    return sum([fibonacci(n) for n in range(35) if fibonacci(n) % 2 == 0])


def problem3():
    return max(list_prime_factors(600851475143))


def problem4():
    answer = []
    for i in range(100, 1000):
        for j in range(i, 1000):
            if (is_palindrome(str(i*j))):
                answer.append(i*j)
    return max(answer)


def problem5():
    return int(reduce(lcm, range(2, 21)))


def problem6():
    n = 100
    sumSquares = (n*(n+1)*(2*n+1))/6
    squareSum = (0.5*n*(n+1))**2
    return squareSum - sumSquares


def problem7():
    return nth_prime(10001)


def problem8():
    answer = 0
    with open('p8.txt', 'r') as number:
        digits = list(map(int, number.read()))
    for i in range(988):
        digitProduct = reduce(mul, digits[i:i+13])
        answer = max(answer, digitProduct)
    return answer


def problem9():
    for a in range(1, 334):
        b = (500-a)/(1-(a/1000))
        if b % 1 == 0:
            return a*b*(1000-(a+b))


def problem10():
    answer = 0
    prime = 2
    while (prime < 2000000):
        answer += prime
        prime = int(next_prime(prime))
    return answer


def problem11():
    answers = []
    with open('p11.txt', 'r') as file:
        grid = file.read().split("\n")
    for row in range(0, 20):
        grid[row] = list(map(int, grid[row].split(" ")))
    for pos in range(0, 16):
        for i in range(0, 16):
            mGrid = grid[pos:pos+4]
            for j in range(0, 4):
                mGrid[j] = mGrid[j][i:i+4]
            answers.append(largest_product(mGrid))
    return max(answers)


def problem12():
    term = 1
    numFactors = 0
    while (numFactors < 500):
        number = term*(term+1)/2
        numFactors = len(list_factors(number))
        term += 1
    return number


def problem13():
    with open('p13.txt', 'r') as file:
        numberList = list(map(int, file.read().split("\n")))
    return str(sum(numberList))[:10]


def problem14():
    answer = 0
    answerLength = 0
    for n in range(1, 1000000):
        if (collatz_length(n) > answerLength):
            answerLength = collatz_length(n)
            answer = n
    return answer


def problem15():
    return lattice_paths(20, 20)


def problem16():
    return sum([int(digit) for digit in str(2**1000)])


def problem17():
    answer = []
    for i in range(1, 1001):
        answer.append(len(num2words(i).replace("-", "").replace(" ", "")))
    return sum(answer)


def problem18():
    with open('p18.txt', 'r') as file:
        triangle = file.read().split("\n")
    for row in range(len(triangle)):
        triangle[row] = list(map(int, triangle[row].split(" ")))
    return max_path_sum(triangle)[0]


def problem19():
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if (weekday(year, month, 1) == 6):
                sundays += 1
    return sundays


def problem20():
    return sum([int(digit) for digit in str(factorial(100))])


def problem21():
    return sum([i for i in range(10000) if is_amicable(i)])


def problem22():
    answer = 0
    nameCount = 1
    with open('p22.txt', 'r') as names:
        nameList = sorted(names.read().replace("\"", "").split(","))
    for name in nameList:
        answer += word_value(name)*nameCount
        nameCount += 1
    return answer


def problem23():
    abundantNums = set()
    answer = 28122*(28123)/2  # sum of numbers 1 to 28122
    for number in range(1, 28123):
        if is_abundant(number):
            abundantNums.add(number)
        for abundant in abundantNums:
            if number-abundant in abundantNums:
                answer -= number
                break
    return answer


def problem24():
    p = permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    p = next(islice(p, 10**6-1, None), None)  # -1 offset
    answer = ''.join(p)
    return int(answer)


def problem25():
    term = 1
    while (digits(fibonacci(term)) < 1000):
        term += 1
    return term


def problem27():
    answer = 0
    answerCount = 0
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            primeCount = 0
            while (is_prime(abs(primeCount**2 + i*primeCount + j))):
                primeCount += 1
            if (primeCount > answerCount):
                answerCount = primeCount
                answer = i*j
    return answer


def problem28():
    return number_spiral(1001)


def problem29():
    return len(set(a**b for (a,b) in product(range(2, 101), repeat=2)))


def problem30():
    answer = 0
    for i in range(32, 295489):
        digitSum = 0
        for j in str(i):
            digitSum += int(j)**5
        if (digitSum == i):
            answer += i
    return answer


def problem34():
    return sum(i for i in range(25, 2177282) if
        sum(factorial(int(j)) for j in str(i)) == i)


def problem35():
    answer = 500000
    for i in range(3, 1000000, 2):
        number = str(i)
        for j in range(0, len(number)):
            if (not is_prime(int(number))):
                answer -= 1
                break
            number = number[1:] + number[:1]
    return answer


def problem36():
    answer = 0
    for number in range(1, 10**6):
        baseTwo = int(str(bin(number))[2:])
        if is_palindrome(number) and is_palindrome(baseTwo):
            answer += number
    return answer


def problem37():
    answer = 0
    primeCount = 0
    for number in count(11, 2):
        isPrime = is_prime(number)
        if (isPrime):
            for j in range(1, len(str(number))):
                cond1 = not is_prime(int(number % 10**j))
                cond2 = not is_prime(int(number / 10**j))
                if (cond1 or cond2):
                    isPrime = False
                    break
        if (isPrime):
            primeCount += 1
            answer += number
        if (primeCount == 11):
            return answer


def problem39():
    answer = 0
    answerCount = 0
    for p in range(1, 1001):
        count = 0
        for a in range(1, int(p/3)):
            b = int((p*(p - 2*a))/(2*(p - a)))
            c = int(p-a-b)
            if (a**2 + b**2 == c**2):
                count += 1
        if (count > answerCount):
            answer = p
            answerCount = count
    return answer


def problem42():
    answer = 0
    triangleNumbers = [0.5*n*(n+1) for n in range(1, 25)]
    with open('p42.txt', 'r') as file:
        wordList = file.read().replace("\"", "").split(",")
    for word in wordList:
        wordValue = word_value(word)
        if (wordValue in triangleNumbers):
            answer += 1
    return answer


def problem43():
    answer = 0
    for n in permutations("0123456789"):
        n = "".join(n)
        if (int(n[1:4]) % 2 == 0 and
                int(n[2:5]) % 3 == 0 and
                int(n[3:6]) % 5 == 0 and
                int(n[4:7]) % 7 == 0 and
                int(n[5:8]) % 11 == 0 and
                int(n[6:9]) % 13 == 0 and
                int(n[7:10]) % 17 == 0):
            answer += int(n)
    return answer


def problem48():
    seriesSum = sum(i**i for i in range(1, 1001))
    return seriesSum % 10**10


def problem49():
    primes = [n for n in range(1000, 10000) if is_prime(n) and
              len(set(str(n))) >= 3]
    primes.remove(1487)
    while True:
        primeCount = 0
        primePermutations = []
        for prime in permutations(str(primes[0])):
            n = int(''.join(prime))
            if n in primes:
                primeCount += 1
                primePermutations.append(primes.pop(primes.index(n)))
        if primeCount >= 3:
            for c in combinations(primePermutations, 3):
                combo = sorted(c)
                if combo[2]-combo[1] == combo[1]-combo[0]:
                    return int(str(combo[0])+str(combo[1])+str(combo[2]))


def problem50():
    primes = [n for n in range(1000000) if is_prime(n)]
    answer = [0, 0]
    for i in range(len(primes)):
        for j in range(i, -1, -1):
            primeCandidate = sum(primes[j:i])
            if primeCandidate > 1000000:
                break
            if is_prime(primeCandidate) and i-j > answer[1]:
                answer = [primeCandidate, i-j]
    return answer[0]


def problem52():
    for number in count(1):
        digits = sorted(str(number))
        sameDigits = True
        for multiple in range(2, 7):
            if sorted(str(number*multiple)) != digits:
                sameDigits = False
                break
        if sameDigits:
            return number


def problem53():
    answer = 0
    for n in range(1, 101):
        for r in range(1, n):
            combos = factorial(n)/(factorial(r)*factorial(n-r))
            if combos > 10**6:
                answer += 1
    return answer


def problem56():
    answer = 0
    for i in range(1, 100):
        for j in range(1, 100):
            digitSum = sum(list(map(int, str(i**j))))
            if (digitSum > answer):
                answer = digitSum
    return answer


def problem57():
    answer = 0
    x = 2
    for expansion in range(1, 1000):
        x = 2 + Fraction(1, x)
        approx = 1 + Fraction(1, x)
        if digits(approx.numerator) > digits(approx.denominator):
            answer += 1
    return answer


def problem62():
    cubeList = {}
    for i in count(1):
        number = "".join(sorted(str(i**3)))
        if (number in cubeList):
            cubeList[number].append(i)
        else:
            cubeList[number] = [i]
        if (len(cubeList[number]) == 5):
            return min(cubeList[number])**3


def problem67():
    with open('p67.txt', 'r') as file:
        triangle = file.read().split("\n")
    for row in range(0, len(triangle)):
        triangle[row] = list(map(int, triangle[row].split(" ")))
    return max_path_sum(triangle)[0]


def problem71():
    expansion = int(10**6 / 7)
    numerator = 3*expansion - 1
    denominator = 7*expansion
    while Fraction(numerator, denominator) < Fraction(3, 7):
        denominator -= 1
    return Fraction(numerator, denominator+1)


def problem97():
    number = 28433*2**7
    for i in range(0, 7830450, 50):
        number *= 2**50
        number %= 10**10
    return int(number+1)


def problem99():
    answerValue = 0
    answerLine = 0
    with open('p99.txt', 'r') as file:
        baseExp = file.read().split("\n")
    for line in range(0, 1000):
        number = list(map(int, baseExp[line].split(",")))
        value = number[1]*log10(number[0])
        if (value > answerValue):
            answerValue = value
            answerLine = line+1
    return answerLine
