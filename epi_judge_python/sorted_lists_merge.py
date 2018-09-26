from test_framework import generic_test

def emplaceAfter(x, y):
    y.next = x.next
    x.next = y

def merge_two_sorted_lists(L1, L2):
    if not L2:
        return L1
    elif not L1:
        return L2

    if L1.data <= L2.data:
        low, high = L1, L2
    else:
        low, high = L2, L1
    head = low
    while low.next and high:
        if low.next.data > high.data:
            temp, high = high, high.next
            emplaceAfter(low, temp)
        low = low.next
    if high:
        low.next = high
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
