from test_framework import generic_test

def has_two_sum(A, target):
    if not A:
        return False
    low, high = 0, len(A) - 1
    while low <= high:
        currSum = A[low] + A[high]
        if currSum == target:
            return True
        elif currSum < target:
            low += 1
        else:
            high -= 1
    return False

def has_three_sum(A, target):
    A.sort()
    for val in A:
        newTarget = target - val
        if has_two_sum(A, newTarget):
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
