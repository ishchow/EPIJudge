from test_framework import generic_test
import random


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k, A):
    def partition(A, low, high, pivotIdx):
        pivotVal = A[pivotIdx]
        newPivotIdx = low
        # Move pivot to the right
        A[pivotIdx], A[high] = A[high], A[pivotIdx]
        # Partition A such that A = [> pivot | <= pivot]
        for i in range(low, high):
            if A[i] > pivotVal:
                A[i], A[newPivotIdx] = A[newPivotIdx], A[i]
                newPivotIdx += 1
        # Switch new pivot with old pivot
        A[high], A[newPivotIdx] = A[newPivotIdx], A[high]
        return newPivotIdx

    low, high = 0, len(A) - 1
    while low <= high:
        pivotIdx = random.randint(low, high)
        newPivotIdx = partition(A, low, high, pivotIdx)
        if newPivotIdx == (k - 1):
            return A[newPivotIdx]
        elif newPivotIdx < (k - 1):
            low = newPivotIdx + 1
        else: # newPivotIdx > (k - 1)
            high = newPivotIdx - 1

    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("kth_largest_in_array.py",
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
