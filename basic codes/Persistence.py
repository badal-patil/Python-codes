"""
Function, persistence, that takes
in a positive parameter num and returns
its multiplicative persistence,
which is the number of times you must multiply
the digits in num until you reach a single digit.

The doctest module searches for pieces of text that look like interactive Python sessions, and then executes those sessions to verify that they work exactly as shown. 
"""


def mul(lists: list) -> int:
    result = 1
    for x in lists:
        result = result * x
    return result


def persistence(n: int) -> int:
    """
    >>> persistence(243)
    2
    """
    a = list(str(n))
    count = 0
    while len(a) != 1:
        a = list(str(mul(map(int, a))))
        count = count + 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()


"""
[+] https://docs.python.org/3/library/doctest.html

Output:
(base) badpat@88665a0dfb70 ~ % /usr/local/bin/python3.11 /Users/badpat/Desktop/knet-neptune/Persistence.py -v 
Trying:
    persistence(243)
Expecting:
    2
ok
2 items had no tests:
    __main__
    __main__.mul
1 items passed all tests:
   1 tests in __main__.persistence
1 tests in 3 items.
1 passed and 0 failed.
Test passed.
"""
