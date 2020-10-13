"""
148. Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # O(nlogn) time, O(n) space
    def sortList(self, head: ListNode) -> ListNode:
        cur = head
        temp = []

        while cur:
            temp.append(cur.val)
            cur = cur.next

        temp.sort()

        dummy = ListNode(-1)
        cur = dummy
        for v in temp:
            cur.next = ListNode(v)
            cur = cur.next

        return dummy.next

    # Bubble Sort: O(n^2) time, O(1) space
    def sortList(self, head: ListNode) -> ListNode:
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next

        i = 0
        while i < N:
            j = 0
            cur = head
            while j < N - i and cur.next:
                if cur.val > cur.next.val:
                    # swap values
                    cur.val, cur.next.val = cur.next.val, cur.val
                cur = cur.next
                j += 1
            i += 1
        return head

    # Merge Sort: O(nlogn) time
    def sortList(self, head: ListNode) -> ListNode:
        # base case:
        if not head or not head.next:
            return head

        # split the list and get the midpoint
        mid = self.midPoint(head)

        # left and right recursive
        left = self.sortList(head)
        right = self.sortList(mid)

        # merge
        return self.merge(left, right)

    def midPoint(self, head):
        # split linked list with fast & slow pointers
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        # return the mid node
        return mid

    def merge(self, left, right):
        dummy = cur = ListNode(-1)
        while left and right:
            if left.val < right.val:
                cur.next = left
                cur = cur.next
                left = left.next
            else:
                cur.next = right
                cur = cur.next
                right = right.next

        # append the rest of right or left to the merged list
        cur.next = left or right
        return dummy.next
