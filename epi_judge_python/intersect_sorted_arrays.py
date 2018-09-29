from test_framework import generic_test


def intersect_two_sorted_arrays(A, B):
    if not A or not B:
        return []
    if (len(A) == 1) and (len(B) == 1):
        return A[0] if A == B else []
    intrsxn = []
    if A[0] < B[0]:
        low, high = iter(A), iter(B)
    else:
        low, high = iter(B), iter(A)
    low = next(low, None)
    high = next(high, None)
    while low and high:
        if low < high:
            low = next(low, None)
        elif low == high:
            if (not intrsxn) or (intrsxn[-1] != low):
                intrsxn.append(low)
            low = next(low, None)
            high = next(high, None)
        else:
            high = next(high, None)
    return intrsxn


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
