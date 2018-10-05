from test_framework import generic_test
from collections import defaultdict

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    if len(letter_text) > len(magazine_text):
        return False
    letterChToFreq = defaultdict(int)
    for ch in letter_text:
        letterChToFreq[ch] += 1

    for ch in magazine_text:
        if ch in letterChToFreq:
            letterChToFreq[ch] -= 1
            if letterChToFreq[ch] == 0:
                del letterChToFreq[ch]
            if not letterChToFreq:
                break
    return not letterChToFreq


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
