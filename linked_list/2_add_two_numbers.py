"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(-1)
        cur = dummy_head
        p = l1
        q = l2
        carry = 0
        while p or q:
            i = p.val if p else 0
            j = q.val if q else 0

            s = i + j + carry

            if s >= 10:
                carry = 1
                remainder = s % 10
                cur.next = ListNode(remainder)
            else:
                carry = 0
                cur.next = ListNode(s)

            cur = cur.next
            if p:
                p = p.next
            if q:
                q = q.next

         # Need to check if carry == 1
        if carry:
            cur.next = ListNode(carry)

        return dummy_head.next
