import doctest, math

def is_prime(number):
    '''
    >>> is_prime(23)
    True
    >>> is_prime(24)
    False
    >>> is_prime(25)
    False
    >>> is_prime(17)
    True
    >>> is_prime(19)
    True
    '''
    if number < 2:
        # special case: 0 and 1
        return False

    for divisor in range(2, int(math.sqrt(number) + 1)):
        if number % divisor == 0:
            return False
    return True

def nth_prime(nth):
    '''
    >>> nth_prime(1)
    2
    >>> nth_prime(2)
    3
    >>> nth_prime(3)
    5
    >>> nth_prime(4)
    7
    >>> nth_prime(5)
    11
    '''
    if nth == 1:
        return 2

    primes_found = 1
    prime_candidate = 3
    while primes_found != nth:
        if is_prime(prime_candidate):
            primes_found += 1
        prime_candidate += 2

    return prime_candidate - 2


doctest.testmod()