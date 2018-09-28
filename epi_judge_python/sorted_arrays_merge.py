from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays):
    if not sorted_arrays:
        return []
    toVisit = [0 if arr else -1 for arr in sorted_arrays]
    heap = [(arr[0], arrIdx) for (arrIdx, arr) in enumerate(sorted_arrays) if arr]
    heapq.heapify(heap)
    mergedList = []
    while heap:
        (val, listIdx) = heapq.heappop(heap)
        mergedList.append(val)
        toVisit[listIdx] += 1
        elemIdx = toVisit[listIdx]
        if elemIdx < len(sorted_arrays[listIdx]):
            val = sorted_arrays[listIdx][elemIdx]
            heapq.heappush(heap, (val,listIdx))
    return mergedList


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
