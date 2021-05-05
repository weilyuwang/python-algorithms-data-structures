"""
23. Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

"""
from queue import PriorityQueue

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Time complexity : O(NlogN) 
        where N is the total number of nodes.

        Space complexity : O(N).
        """
        self.nodes = []
        dummy_head = ListNode(-1)
        cur = dummy_head
        # Add all nodes into the list
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next

        for x in sorted(self.nodes):
            cur.next = ListNode(x)
            cur = cur.next

        return dummy_head.next

        
    # O(logK) Divide and Conquer
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
            def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.merge2Lists(l1, l2))
                
            lists = mergedLists
            
        return lists[0]
         
    def merge2Lists(self, l1, l2):
        dummy = tail = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next=l1
        else:
            tail.next=l2
        return dummy.next
