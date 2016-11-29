
better_keep_if = 1  # REPLACE None WITH 1 or 2

better_keep_if_explanation = """
Version 1 is better because i += 1 statement is outside of condition statment 'if' so i is
increased by 1 even if i does not meet the condition. On the other hand, in version 2,
although it does the same thing i += 1 is repeated with else: which is redundant.
"""


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    if n == 0:
        return 1
    else:
        return n if n <= 3 else g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)
    

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    i, total = 4, 4
    if n <= 3:
        return n
    else:
        first, second, third = 3, 2, 1
        total = 0
        while i <= n:
            total = first + second * 2 + third * 3
            first, second, third = total, first, second
            i += 1
    return total


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    def count(k, l, t):
        if k == n:
            return l
        else:
            if k % 7 == 0 or has_seven(k):
                return count(k + 1, l - 1, 0) if t == 1 else count(k + 1, l + 1, 1)
            else:
                return count(k + 1, l + 1, 1) if t == 1 else count(k + 1, l - 1, 0)
    return count(1, 1, 1)

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    l = 0
    while pow(2, l) < amount:
        l += 1
        def count_partitions(n, m):
            if n == 0:
                return 1
            elif n < 0 or m < 0:
                return 0
            else:
                with_m = count_partitions(n - pow(2, m), m)
                without_m = count_partitions(n, m - 1)
                return with_m + without_m
    return count_partitions(amount, l)

def towers_of_hanoi(n, start, end):
    """Print the moves required to solve the towers of hanoi game, starting
    with n disks on the start pole and finishing on the end pole.

    The game is to assumed to have 3 poles.

    >>> towers_of_hanoi(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> towers_of_hanoi(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> towers_of_hanoi(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 0 < start <= 3 and 0 < end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    one = ([i for i in range(1, n + 1)], '1')
    two = ([], '2')
    three = ([], '3')
    def hanoi_print(k, start_list, hold_list, end_list):
        if k > 0:    
            hanoi_print(k - 1, start_list, end_list, hold_list)
            if start_list[0]:
                print('Move the top disk from rod ' + start_list[1] + ' to rod ' + end_list[1])
                end_list[0].append(start_list[0].pop())
            hanoi_print(k - 1, hold_list, start_list, end_list)
    hanoi_print(n, one, two, three)   
    


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'

