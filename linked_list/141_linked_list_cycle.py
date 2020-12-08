"""
141. Linked List Cycle

Given head, the head of a linked list,
determine if the linked list has a cycle in it.


The space complexity can be reduced to O(1) by considering two pointers at different speed
- a slow pointer and a fast pointer.
The slow pointer moves one step at a time while the fast pointer moves two steps at a time.

If there is no cycle in the list, the fast pointer will eventually reach the end
and we can return false in this case.

Now consider a cyclic list and imagine the slow and fast pointers are
two runners racing around a circle track. The fast runner will eventually meet the slow runner.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
