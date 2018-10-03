from test_framework import generic_test
from list_node import ListNode

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    slow, fast, jumpCnt = L, L, 0
    for _ in range(k):
        if not fast.next:
            break
        fast, jumpCnt = fast.next, jumpCnt + 1
    if jumpCnt < k:
        delNode, L = L, L.next
        delNode.next = None
        return L
    while fast.next:
        fast, slow = fast.next, slow.next
    delNode = slow.next
    slow.next = delNode.next
    delNode.next = None
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
