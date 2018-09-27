from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    mergedList = []
    heapq.heapify(mergedList)
    for sL in sorted_arrays:
        for elem in sL:
            heapq.heappush(mergedList, elem)
    mergedList = [heapq.heappop(mergedList) for _ in range(len(mergedList))]
    return mergedList


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
