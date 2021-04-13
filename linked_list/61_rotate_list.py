'''
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]
 
Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # need to get the length of the linked list
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
            
        k = k % n
        if k == 0:
            return head
        
        # move to the pivot and perform the rotate
        cur = head
        for i in range(n - k - 1):
            cur = cur.next
        
        newHead = cur.next
        cur.next = None
        tail.next = head
        
        return newHead