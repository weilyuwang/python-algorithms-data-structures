"""
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:

Input: 1->1->1->2->3
Output: 2->3

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
        if not head:
            return None

        # find duplicates:
        duplicates = {}

        cur = head
        while cur:
            if cur.val in duplicates:
                duplicates[cur.val] += 1
            else:
                duplicates[cur.val] = 1

            cur = cur.next

        dummy_head = ListNode(-1)
        dummy_head.next = head

        prev = dummy_head
        cur = head

        while cur:
            if cur.val in duplicates and duplicates[cur.val] > 1:
                # duplicates - skip/remove cur node
                prev.next = cur.next
            else:
                prev = cur

            cur = cur.next

        return dummy_head.next

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        This only works for sorted linked list
        """
        if not head:
            return None

        dummy_head = ListNode(-1)
        dummy_head.next = head

        cur = dummy_head
        while cur.next and cur.next.next:
            # if encounter duplicates after current node
            if cur.next.val == cur.next.next.val:
                prev_val = cur.next.val
                while cur.next and cur.next.val == prev_val:
                    # Keep skipping duplicates until find a new val
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy_head.next
