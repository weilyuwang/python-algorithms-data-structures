'''
919 · Meeting Rooms II

Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
Example2

Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
'''


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        
        # Sort by start time
        intervals.sort(key = lambda x : x.start)

        meeting_rooms = 1

        # Push end times to the min heap
        # once we find a meeting A that has start time < (earliest/smallest) end time
        # in the min heap, we can pop that end time off the heap

        heap = [intervals[0].end]

        for interval in intervals[1:]:
            if heap[0] < interval.start:
                # pop the earliest end time 
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            meeting_rooms = max(meeting_rooms, len(heap))
        
        return meeting_rooms
