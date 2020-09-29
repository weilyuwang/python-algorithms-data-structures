"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Recursive
    # Every recursion call is responsible for swapping a pair of nodes
    def swapPairs(self, head: ListNode) -> ListNode:
        # base case
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next

        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node

    # Iterative
    # We break the linked list into pairs by jumping in steps of two.
    # After swapping a pair of nodes, say A and B,
    # we need to link the node B to the node that was right before A.
    def swapPairs(self, head: ListNode) -> ListNonde:
        # Dummy node acts as the prevNode for the head node
        # of the list and hence stores pointer to the head node.
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next

            # Swap (Need to link the new pair to the previous pair)
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next

        # Return the new head
        return dummy.next
