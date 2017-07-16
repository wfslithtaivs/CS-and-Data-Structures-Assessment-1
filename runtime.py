def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [ const + n ~ O(n) ]
    """

    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [n + n = 2n ~ 2 * O(n) ~ O(n)]

    """

    if "hippo" in animals or "platpypus" in animals:
        return True
    else:
        return False


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [ n + n^2 = n(n+1) ~ n*n = n^2 ~ O(n^2) - in a worst case, but in average - O(n)]

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)

    for x in s: # n
        if -x in s: # worst case O(n), but average O(1) - https://wiki.python.org/moin/TimeComplexity
            result.append([-x, x])

    return result


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [ n*n ~ O(n^2)  ]

    """

    result = []

    for x in numbers: # n
        for y in numbers: # n
            if x == -y: # const
                result.append((x, y)) # const
    return result


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [ n * (n + const + const + n + n) = n * (3n + 2const) ~ n^2 ~ O(n^2) }               ]

    """

    result = []

    for x in numbers: # n
        for y in numbers: # n
            if x == -y and (x, y) not in result and (y, x) not in result: # const + n + n
                result.append((x, y))
    return result
