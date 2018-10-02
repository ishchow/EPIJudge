import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from bst_node import BstNode


def build_min_height_bst_from_sorted_array(A):
    def getRoot(A, low, high):
        if low > high:
            return None
        mid = low + ((high - low) // 2)
        return BstNode(A[mid], getRoot(A, low, mid - 1), getRoot(A, mid + 1, high))
    return getRoot(A, 0, len(A) - 1)


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure("Result binary tree mismatches input array")
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "bst_from_sorted_array.py", 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
