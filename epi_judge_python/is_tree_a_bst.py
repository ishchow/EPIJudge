from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    prev = float('-inf')
    def helper(root):
        nonlocal prev
        if not root:
            return
        helper(root.left)
        if prev == float('inf'):
            return
        elif root.data < prev:
            prev = float('inf')
            return
        prev = root.data
        helper(root.right)
    helper(tree)
    return prev < float('inf')

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
