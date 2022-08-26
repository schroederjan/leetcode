""" Merge Two Sorted Lists """
# https://realpython.com/linked-lists-python/
# https://leetcode.com/problems/merge-two-sorted-lists/discuss/759870/Python3-Solution-with-a-Detailed-Explanation-dummy-explained

from typing import Optional, List
from linked_list import linkedList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
            self,
            list1: Optional[ListNode],
            list2: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == '__main__':

    def list_to_llist(test_list: list):
        llist = linkedList()
        for var in test_list:
            llist.insertAtEnd(var)
        return llist

    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]

    llist_1 = list_to_llist(list_1)
    llist_2 = list_to_llist(list_2)
    #
    #  print(llist_1)
    #  print(llist_1.head.val)
    #  print(llist_1.head.next.val)
    #  print(llist_2)

    def mergeTowLists(l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1 < l2:
                cur.next = l1.val
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    def test(l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            print(l1)
        return None

    #  test(llist_1, llist_2)
    #mergeTowLists(llist_1, llist_2)

    def create_linked_list(l: List[int]):
        """ TODO """
        ll = []
        for v in l:
            head = ListNode(v)
            ll.append(head)
        return ll

    llist_1 = create_linked_list(list_1)
    llist_2 = create_linked_list(list_2)

    print(llist_1[0].val)
    print(llist_1[0].next)
    print(llist_1[1].val)
    print(llist_1[1].next)
