from test_framework import generic_test

def search_first_of_k(A, k):
    if not A:
        return -1
    low, high, lowest = 0, len(A) - 1, -1
    while low <= high:
        mid = low + ((high - low) // 2)
        if A[mid] < k:
            low = mid + 1
        elif A[mid] == k:
            lowest = mid
            high = mid - 1
        else:
            high = mid - 1
    return lowest

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
