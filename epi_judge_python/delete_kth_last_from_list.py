from test_framework import generic_test
from list_node import ListNode

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    sz, curr = 0, L
    while curr:
        sz += 1
        curr = curr.next
    jumpSz = sz - k
    if jumpSz == 0:
        delNode, L = L, L.next
        delNode.next = None
        return L
    dummy = ListNode(None, L)
    prevNode, delNode = dummy, L
    for _ in range(jumpSz):
        prevNode, delNode = prevNode.next, delNode.next
    prevNode.next = delNode.next
    delNode.next = None
    dummy.next = None
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
