"""
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        This will remove duplicates for any sorted/unsorted linked lists
        """

        prev = None
        cur = head

        duplicates = {}

        while cur:
            if cur.val in duplicates:
                # remove node
                prev.next = cur.next
                cur = None
            else:
                # encounter a new val
                duplicates[cur.val] = 1
                prev = cur

            cur = prev.next

        return head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        For sorted linked list only:
        """

        if not head:
            return None

        prev = head
        cur = head.next

        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return head
