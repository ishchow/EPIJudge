from test_framework import generic_test
from collections import namedtuple

BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ['balanced', 'height'])

def is_balanced_binary_tree(tree):
    def helper(root):
        if not root:
            return BalancedStatusWithHeight(True, -1)

        leftResult, rightResult = helper(root.left), helper(root.right)
        if not leftResult.balanced or not rightResult.balanced:
            return BalancedStatusWithHeight(False, 0)
        is_balanced = abs(leftResult.height - rightResult.height) <= 1
        height = max(leftResult.height, rightResult.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return helper(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
