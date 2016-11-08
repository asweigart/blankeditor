import doctest

def is_palindrome(number):
    '''
    >>> is_palindrome(1234)
    False
    >>> is_palindrome(9009)
    True
    >>> is_palindrome(4)
    True
    '''
    numAsList = list(str(number))
    return numAsList == list(reversed(numAsList))


def largest_palindrome(max_factor, min_factor=0):
    largest_so_far = 0
    largest_so_far_factors = set()

    for factorA in range(min_factor, max_factor + 1):
        for factorB in range(min_factor, max_factor + 1):
            product = factorA * factorB
            if is_palindrome(product):
                if product > largest_so_far:
                    largest_so_far = product
                    largest_so_far_factors = {factorA, factorB}
                #elif product == largest_so_far:
                #    largest_so_far_factors.add(factorA)
                #    largest_so_far_factors.add(factorB)
    return (largest_so_far, largest_so_far_factors)


def smallest_palindrome(max_factor, min_factor=0):
    smallest_so_far = max_factor * max_factor
    smallest_so_far_factors = set()

    for factorA in range(min_factor, max_factor + 1):
        for factorB in range(min_factor, max_factor + 1):
            product = factorA * factorB
            if is_palindrome(product):
                if product < smallest_so_far:
                    smallest_so_far = product
                    smallest_so_far_factors = {factorA, factorB}
    return (smallest_so_far, smallest_so_far_factors)



doctest.testmod()