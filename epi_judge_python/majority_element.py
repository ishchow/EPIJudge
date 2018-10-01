from test_framework import generic_test
from collections import defaultdict

def majority_search(stream):
    candidate = ''
    candidateCount = 0
    for elem in stream:
        if candidateCount == 0:
            candidate = elem
            candidateCount = 1
        elif elem == candidate:
            candidateCount += 1
        else: # elem != candidate
            candidateCount -= 1
    return candidate


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
