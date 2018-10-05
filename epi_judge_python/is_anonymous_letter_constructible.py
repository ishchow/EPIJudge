from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    if len(letter_text) > len(magazine_text):
        return False
    magChToFreq = {}
    for ch in magazine_text:
        if ch not in magChToFreq:
            magChToFreq[ch] = 0
        magChToFreq[ch] += 1

    for ch in letter_text:
        if ch not in magChToFreq:
            return False
        magChToFreq[ch] -= 1
        if magChToFreq[ch] < 0:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
