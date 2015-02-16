from eulermaths import *
from gmpy2 import is_prime, next_prime, lcm
from math import factorial, log10
from operator import mul
from functools import reduce
from num2words import num2words
from itertools import count
from calendar import weekday


def problem1():
    answer = []
    answer.extend(list_multiples(3, upperBound=1000))
    answer.extend(list_multiples(5, upperBound=1000))
    return sum(set(answer))


def problem2():
    answer = 0
    for i in range(2, 35):
        value = fibonacci(i)
        if (value % 2 == 0):
            answer += value
    return answer


def problem3():
    return max(list_prime_factors(600851475143))


def problem4():
    answer = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            number = i*j
            if (str(number) == str(number)[::-1] and number > answer):
                answer = number
    return answer


def problem5():
    return int(reduce(lcm, range(2, 21)))


def problem6():
    sumSquares = 0
    squareSum = 0
    for i in range(1, 101):
        sumSquares += i**2
        squareSum += i
    squareSum = squareSum**2
    return squareSum - sumSquares


def problem7():
    return nth_prime(10001)


def problem8():
    answer = 0
    digits = []
    with open('p8.txt', 'r') as number: 
        digits.extend(number.read())
        digits = list(map(int, digits))
    for i in range(0, 988):
        digitProduct = reduce(mul, digits[i:i+13])
        if (digitProduct > answer):
            answer = digitProduct
    return answer


def problem9():
    for a in range (1, 334):
        for b in range(a, 666):
            if (a**2 + b**2 == (1000-a-b)**2):
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
    triangleTerm = 1
    factors = 0
    while (factors < 500):
        triangleNumber = 0.5*triangleTerm*(triangleTerm+1)
        factors = len(list_factors(triangleNumber))
        triangleTerm += 1
    return triangleNumber


def problem13():
    with open('p13.txt', 'r') as file:
        numberList = list(map(int, file.read().split("\n")))
    return str(sum(numberList))[:10]


def problem14():
    answer = 0
    answerLength = 0
    for number in range(1, 1000000):
        length = collatz_length(number)
        if (length > answerLength):
            answerLength = length
            answer = number
    return answer


def problem15():
    return lattice_paths(20, 20)


def problem16():
    return sum([int(digit) for digit in str(2**1000)])
        

def problem17():
    answer = 0
    for i in range(1, 1001):
        numberWord = num2words(i).replace("-", "").replace(" ", "")
        answer += len(numberWord)
    return answer


def problem18():
    with open('p18.txt', 'r') as file:
        triangle = file.read().split("\n")
    for row in range(0, len(triangle)):
        triangle[row] = list(map(int, triangle[row].split(" ")))
    return max_path_sum(triangle)[0]


def problem19():
    sundayCount = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if (weekday(year, month, 1) == 6):
                sundayCcount += 1
    return sundayCcount

    
def problem20():
    return sum([int(digit) for digit in str(factorial(100))])


def problem21():
    answer = 0
    for i in range(1, 10000):
        if (is_amicable(i)):
            answer += i
    return answer


def problem22():
    answer = 0
    nameCount = 1
    with open('p22.txt', 'r') as names:
        nameList = names.read().replace("\"", "").split(",")
        nameList = sorted(nameList)
    for name in nameList:
        nameValue = word_value(name)*nameCount
        answer += nameValue
        nameCount += 1
    return answer

            
def problem25():
    term = 0
    value = 0
    while (len(str(value)) < 1000):
        term += 1
        value = fibonacci(term)
    return term


def problem27():
    answer = 0
    answerCount = 0
    primeCount = 0
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            while (is_prime(abs(primeCount**2 + i*primeCount + j))):
                primeCount += 1
            if (primeCount > answerCount):
                answerCount = primeCount
                answer = i*j
            primeCount = 0
    return answer


def problem28():
    return number_spiral(1001)


def problem29():
    answer = []
    for a in range(2, 101):
        for b in range(2, 101):
            answer.append(a**b)
    return len(set(answer))


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
    answer = 0
    for i in range(25, 2177282):   
        if (sum([factorial(int(j)) for j in str(i)]) == i):
            answer += i
    return answer


def problem35():
    answer = 1
    for i in range(3, 1000000, 2):
        number = str(i)
        isCircular = True
        for j in range(0, len(number)):
            if (not is_prime(int(number))):
                isCircular = False
                break
            number = number[1:] + number[:1]
        if (isCircular):
            answer += 1
    return answer


def problem37():
    answer = 0
    primeCount = 0
    for number in count(11, 2):
        isPrime = is_prime(number)
        if (isPrime):
            for j in range(1, len(str(number))):
                if (not is_prime(int(number%10**j)) or
                    not is_prime(int(number/10**j))
                    ):
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
    for p in range (1, 1001):
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
        

def problem48():
    seriesSum = 0
    for i in range(1, 1001):
        seriesSum += i**i
    return str(seriesSum)[-10:]


def problem56():
    answer = 0
    for i in range(1, 100):
        for j in range(1, 100):
            digitSum = sum(list(map(int, str(i**j))))
            if (digitSum > answer):
                answer = digitSum
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


def problem99():
    answerValue = 0
    answerLine = 0
    with open('p99.txt', 'r') as file:
        baseExp = file.read().split("\n")
    for line in range(0, 1000):
        baseExp[line] = list(map(int, baseExp[line].split(",")))
        value = baseExp[line][1]*log10(baseExp[line][0])
        if (value > answerValue):
            answerValue = value
            answerLine = line+1
    return answerLine
