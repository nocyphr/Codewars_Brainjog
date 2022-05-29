import math


def is_prime(num):
    # init to true if num = 2
    isPrime = (num == 2)

    # only calculate squareroot of num if num > 0
    if num > 0:
        root = math.ceil(math.sqrt(num)) + 1

    # preemptive check if number is divisible by 2 (while not being 2)
    isOdd = (num > 2) * (num % 2 != 0)

    # loop over series between num and root of num. No even division found returns True for Prime found,
    # otherwise return current value of isPrime
    if isOdd:
        for i in range(3, root):
            if num % i == 0:
                return False
        return True
    else:
        return isPrime