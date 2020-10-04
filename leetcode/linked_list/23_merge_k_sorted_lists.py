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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        Leverage Priority Queue to optimize the comparison process

        Time complexity : O(Nlogk) 
        where N is the total number of nodes, k is the number of lists.

        Space complexity : O(N).
        """

        """
        Note that in the event that two or more of the lists have the same val,
        the queue module will compare the second element in the priority queue which is a ListNode object 
        (and this is not a comparable type).

        To solve for this issue, instead of push (node.val, node) into the queue,
        we can store (node.val, list_index, node) to account for this edge case,
        - i.e. use the list index as a tie-breaker.
        """

        # Keep a priority queue of size k (# of lists)
        # put() & get() both take O(logk)
        pq = PriorityQueue()
        dummy_head = ListNode(-1)
        cur = dummy_head

        idx = 0

        for l in lists:
            if l:
                # Put the top element of each list onto the priority queue
                pq.put((l.val, idx, l))
                idx += 1

        while not pq.empty():
            # Get the smallest element from priority queue
            val, _, node = pq.get()  # we dont care about the index of the list

            cur.next = ListNode(val)
            cur = cur.next

            # the next node to push onto pq is node.next
            node = node.next
            if node:
                pq.put((node.val, idx, node))
                idx += 1

        return dummy_head.next
