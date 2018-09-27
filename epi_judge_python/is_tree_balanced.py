from test_framework import generic_test


def is_balanced_binary_tree(tree):
    def helper(root):
        if not root:
            return -1
        leftHeight = 1 + helper(root.left)
        rightHeight = 1 + helper(root.right)
        return abs(leftHeight - rightHeight)
    return helper(tree) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
