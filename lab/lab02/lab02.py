"""Required questions for lab 2"""

## Boolean Operators ##

# Q4
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    "*** YOUR CODE HERE ***"
    return x > 0 and y > 0


## while Loops ##

# Q7
def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    i = n
    while i >= 1:
        if n % i == 0:
            print(i)
        i -= 1


# Q8
def fib(n):
    """Returns the nth Fibonacci number.

    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(100)
    354224848179261915075
    """
    "*** YOUR CODE HERE ***"
    step = 2
    lastfib = 0
    currentfib = 1
    if n == 0:
        return lastfib
    elif n == 1:
        return currentfib
    else:
        while step <= n:
            nextfib = lastfib + currentfib
            lastfib = currentfib
            currentfib = nextfib
            step += 1
    return nextfib