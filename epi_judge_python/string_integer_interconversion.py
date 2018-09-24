from test_framework import generic_test
from test_framework.test_failure import TestFailure
from math import floor, log10
import string

def int_to_string(x):
    if x == 0:
        return "0"

    x, isNegative = abs(x), x < 0
    result = []
    while x:
        digit = ord('0') + (x % 10)
        result.append(chr(digit))
        x //= 10
    if isNegative:
        result.append('-')
    return ''.join(reversed(result))

def string_to_int(s):
    result = 0
    for i in range(s[0] == '-', len(s)):
        result = (result * 10) + (ord(s[i]) - ord('0'))
    if s[0] == '-':
        result = -result
    return result

def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
