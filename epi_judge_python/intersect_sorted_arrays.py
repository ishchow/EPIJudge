from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    if not A or not B:
        return []
    if (len(A) == 1) and (len(B) == 1):
        return A[0] if A == B else []
    intrsxn = []
    if A[0] < B[0]:
        lowIt, highIt = iter(A), iter(B)
    else:
        lowIt, highIt = iter(B), iter(A)
    # Start low and high at beginning of respective arrays, or none if empty
    low = next(lowIt, None)
    high = next(highIt, None)
    i = 0
    while None not in [low, high]:
        if low < high:
            low = next(lowIt, None)
        elif low == high:
            if (not intrsxn) or (intrsxn[-1] != low):
                intrsxn.append(low)
            low = next(lowIt, None)
            high = next(highIt, None)
        else:
            high = next(highIt, None)
        i += 1
    return intrsxn


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
