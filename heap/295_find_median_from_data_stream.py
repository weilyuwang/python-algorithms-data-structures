'''
295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

'''

import heapq
class MedianFinder:

    def __init__(self):
        """
        keep two heaps (or priority queues):

        Max-heap: small has the smaller half of the numbers.
        Min-heap: large has the larger half of the number
        """
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        """
        We use heapq class to implement Heaps in Python. 
        By default Min Heap is implemented by this class.
        But we multiply each value by -1 so that we can use it as MaxHeap.
        """
        small, large = self.heaps
        
        # push to small first by default
        heapq.heappush(large, -heapq.heappushpop(small, -num))
        
        # keep size even (let len(small) >= len(large))
        if len(large) > len(small):
            val = heapq.heappop(large)
            heapq.heappush(small, -val)

    def findMedian(self) -> float:
        small, large = self.heaps
        
        if len(small) > len(large):
            return -small[0]

        return (-small[0] + large[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()