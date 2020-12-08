"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of 
the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Iterative
        """
        dummy_head = ListNode(-1)

        prev = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 or l2

        return dummy_head.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Recursive
        """

        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
