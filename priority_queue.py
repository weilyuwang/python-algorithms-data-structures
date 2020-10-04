"""
Priority Queue in Python

1. Use heapq module
   The heapq implements a min-heap sort algorithm suitable for use with Python's lists.

2. Use queue.PriorityQueue 
   Note: The PriorityQueue uses the same heapq implementation internally
"""

# Use heapq
import heapq
customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
while customers:
    print(heapq.heappop(customers))
# Will print names in the order: Riya, Harry, Charles, Stacy.

# Can use heapify() to turn a list into a heap.
a = [3, 5, 1, 2, 6, 8, 7]
heapq.heapify(a)
print(a)  # [1, 2, 3, 5, 6, 8, 7]

# Use queue.PriorityQueue
from queue import PriorityQueue
# we initialise the PQ class instead of using a function to operate upon a list.
customers = PriorityQueue()
customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))
while not customers.empty():
    print(customers.get())
# Will print names in the order: Riya, Harry, Charles, Stacy.
