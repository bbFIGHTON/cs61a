def digit(n, k):
    """Return the k-th digit from the right of n for positive integers n and k.

    >>> digit(3579, 2)
    5
    >>> digit(3579, 0)
    9
    >>> digit(3579, 10)
    0
    """
    '''
    rest = n
    if rest // pow(10,k) == 0:
        return 0
    elif k == 0:
        return rest % pow(10,k+1)
    else:
        return rest // pow(10,k) - (rest // pow(10,k+1) * 10)
    '''
    return n // pow(10,k) % 10


def middle(a, b, c):
    """Return the number among a, b, and c that is not the smallest or largest.
    Assume a, b, and c are all different numbers.

    >>> middle(3, 5, 4)
    4
    >>> middle(30, 5, 4)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(3, 5, 40)
    5
    >>> middle(30, 5, 40)
    30
    """
    return a + b +c - max(a,b,c) - min(a,b,c)


def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    '''
    if k <= 1:
        return pow(n,k) 
    total = n

    while k > 1:
        n -= 1
        k -= 1
        total *= n
        
    return total
    '''

    total, stop = 1, n-k
    while n > stop:
        total, n = total * n, n-1
    return total

    "*** YOUR CODE HERE ***"


def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 that are divisible by 7
    >>> c
    0
    """

    count = 0
    i = 1
    while i <= n:
        if i % k == 0:
            print(i)
            count += 1
        i += 1
    return count

    "*** YOUR CODE HERE ***"


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """

    total = 0
    while y > 0:
        total = total + y % 10
        y = y // 10
    return total
    "*** YOUR CODE HERE ***"


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    rest = n
    while rest > 0:
        i,rest = rest % 10, rest // 10
        if i == rest % 10 == 8:
            return True
    return False 
    
    "*** YOUR CODE HERE ***"

