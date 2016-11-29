# Q1
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + skip_add(n - 2)

# Q6
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a < 0 or b < 0:
        return 1
    elif a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(b - a, a)

# Q7
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    def help(x, n):
        print(x)
        if x == 1:
            return n + 1
        elif x % 2 == 0:
            return help(x // 2, n + 1)
        else:
            return help(x * 3 + 1, n + 1)
    return help(n, 0)

# Q8
def fibonacci(n):
    """Return the nth fibonacci number.

    >>> fibonacci(11)
    89
    >>> fibonacci(5)
    5
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Q9
def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 and n == 1:
        return 1
    else:
        if m == 1 and n > 1:
            return paths(m, n - 1)
        elif m > 1 and n == 1:
            return paths(m - 1, n)
        else:
            move_up = paths(m - 1, n)
            move_down = paths(m , n - 1)
            return move_up + move_down
        