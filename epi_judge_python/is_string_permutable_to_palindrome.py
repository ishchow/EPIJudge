from test_framework import generic_test
from collections import defaultdict

def can_form_palindrome(s):
    if len(s) <= 1:
        return True
    chToModFreq = defaultdict(int)
    for ch in s:
        chToModFreq[ch] = (chToModFreq[ch] + 1) % 2
    modSum = sum(chToModFreq.values())
    return modSum == (len(s) % 2)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
