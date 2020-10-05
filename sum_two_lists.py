"""
Sum two linked lists:

5 -> 6 -> 3
+
8 -> 4 -> 2
=
3 -> 1 -> 6

i.e. 365 + 248 = 613

Note: the head of the linked list represents the least significant digit

365 + 48:

5 -> 6 -> 3
+
8 -> 4

512 + 638:

2 -> 1 -> 5
8 -> 3 -> 6

0 -> 5 -> 1 -> 1
"""


from singly_linked_list import LinkedList


def sum_two_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    p = l1.head
    q = l2.head

    sum_list = LinkedList()

    carry = 0
    while p or q:
        i = p.data if p else 0
        j = q.data if q else 0

        # Calculate carry & remainder
        s = i + j + carry
        if s >= 10:
            carry = 1
            remainder = s % 10
            sum_list.append(remainder)
        else:
            carry = 0
            sum_list.append(s)

        if p:
            p = p.next
        if q:
            q = q.next

    if carry:
        sum_list.append(carry)

    return sum_list


l1 = LinkedList()
l1.append(2)
l1.append(1)
l1.append(5)
l1.print_list()  # 5 -> 1 -> 2 ->


l2 = LinkedList()
l2.append(8)
l2.append(3)
l2.append(6)
l2.print_list()  # 8 -> 3 -> 6 ->

sum_l = sum_two_lists(l1, l2)
sum_l.print_list()  # 0 -> 5 -> 1 -> 1 ->
