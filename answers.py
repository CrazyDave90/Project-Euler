import eulermaths
import functools
import gmpy2


def problem1():
    answer = []
    answer.extend(eulermaths.listMultiples(3, upperBound=1000))
    answer.extend(eulermaths.listMultiples(5, upperBound=1000))
    return sum(set(answer))


def problem2():
    answer = 0
    for n in range(2, 35, 1):
        value = eulermaths.fibonacci(n)
        if (value % 2 == 0):
            answer += value
    return answer
            

def problem3():
    return max(eulermaths.listPrimeFactors(600851475143))


def problem5():
    return int(functools.reduce(gmpy2.lcm, range(2, 21)))


def problem7():
    return eulermaths.nthPrime(10001)


def problem10():
    answer = 0
    prime = 2
    while (prime < 2000000):
        answer += prime
        prime = int(gmpy2.next_prime(prime))
    return answer
        
