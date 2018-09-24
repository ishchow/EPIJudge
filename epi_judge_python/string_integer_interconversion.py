from test_framework import generic_test
from test_framework.test_failure import TestFailure
from math import floor, log10

def digit_to_ch(digit):
    table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    return table.get(digit, None)

def int_to_string(x):
    result = []
    currPow10 = 10 ** (floor(log10(x)) - 1)
    while x:
        digit = x // currPow10
        result.append(digit_to_ch(digit))
        x %= currPow10
        currPow10 //= 10
    return "".join(result)

def string_to_int(str):
    result = 0
    currPow10 = 1
    for i in range(reversed(len(str))):
        ch = str[i]
        if ord(ch) < ord('0') or ord(ch) > ord('9'):
            # TODO: Handle error
            pass
        digit = ord(ch) - ord('0')
        result += (digit * currPow10)
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
