'''
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Empty list
        if not head:
            return None
        
        # Move the two pointers until they reach the proper starting point
        # in the list.
        prev, cur = None, head
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1

        con, tail = prev, cur
        
        # Iteratively reverse the nodes until right becomes 0.
        while right:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            right -= 1
        
        if con:
            con.next = prev
        else: # con could be None
            head = prev
        tail.next = cur
        return head