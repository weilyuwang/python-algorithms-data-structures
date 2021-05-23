'''
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''


from collections import defaultdict
from typing import List


class Solution:
    def canFinishDFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i: [] for i in range(numCourses)}
        
        for course, pre in prerequisites:
            preMap[course].append(pre)
            
        # visitSet: all courses along the current DFS path
        visitSet = set()
        
        def dfs(course):
            # detect loop
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True
            
            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            visitSet.remove(course)
            
            # course can be visited: setpreMap[course] to [] 
            # so that we don't need to dfs on this course later on
            preMap[course] = [] 
            return True
        
        # Run dfs on each course
        for course in range(numCourses):
            if not dfs(course): return False
        return True

    '''
    Topological Sort
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inGoing = defaultdict(set)
        outGoing = defaultdict(set)

        for i, j in prerequisites:
            # j is prerequisite of i (j -> i)
            inGoing[i].add(j)
            outGoing[j].add(i)

        # len(inGoing[i]) == 0 means course i has no prerequisites
        canTake = [i for i in range(numCourses) if len(inGoing[i]) == 0]
        taken = 0
        while len(canTake) > 0:
            take = canTake.pop()
            taken += 1
            for nextCourse in outGoing[take]: # take -> nextCourse
                inGoing[nextCourse].remove(take)
                if len(inGoing[nextCourse]) == 0:
                    canTake.append(nextCourse)
                    
        return taken == numCourses
