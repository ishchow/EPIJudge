from test_framework import generic_test
from collections import defaultdict

def majority_search(stream):
    maxElem = ''
    elemToFreq = defaultdict(int)
    for elem in stream:
        elemToFreq[elem] += 1
        if elemToFreq[elem] > elemToFreq[maxElem]:
            maxElem = elem
    return maxElem


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
