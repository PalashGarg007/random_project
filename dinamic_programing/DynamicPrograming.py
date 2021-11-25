# Dynamic programming
import timeit
""" Dynamic Programming is mainly used when solutions of the same subproblems
    are needed again and again. In dynamic programming, computed solutions to
    subproblems are stored in a table so that these don’t have to be
    recomputed. So Dynamic Programming is not useful when there are no common
    (overlapping) subproblems because there is no point storing the solutions
    if they are not needed again.
"""

##############################################################################
"""
   In fub(n) function compiler has to calculate value of each recursion in
   repeatation thus taking a long time O(fub(n)) = 2^n
"""


def fub(n):
    if n < 2:
        return n
    else:
        return fub(n-1) + fub(n-2)


print(timeit.timeit(lambda: fub(5)))

##############################################################################
"""
   The memoized program for a problem is similar to the recursive version
   with a small modification that looks into a lookup table before computing
   solutions. We initialize a lookup array with all initial values as NIL.
   Whenever we need the solution to a subproblem, we first look into the
   lookup table. If the precomputed value is there then we return that value,
   otherwise, we calculate the value and put the result in the lookup table
   so that it can be reused later.
   Worst time O(mfub(n)) = n
"""


def mfub(n, lookup):
    if n < 2:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = mfub(n-1, lookup) + mfub(n-2, lookup)

    return lookup[n]


lookup = [None]*40
print(timeit.timeit(lambda: mfub(30, lookup)))

##############################################################################
"""
    The tabulated program for a given problem builds a table in bottom-up
    fashion and returns the last entry from the table. For example, for the
    same Fibonacci number, we first calculate fib(0) then fib(1) then fib(2)
    then fib(3), and so on. So literally, we are building the solutions of
    subproblems bottom-up.
    O(tfub(n)) = n
"""


def tfub(n):
    bottomup = [None]*(n+1)
    bottomup[0], bottomup[1] = 0, 1
    for i in range(2, n+1):
        bottomup[i] = bottomup[i-1] + bottomup[i-2]

    return bottomup[n]


print(timeit.timeit(lambda: tfub(30)))
