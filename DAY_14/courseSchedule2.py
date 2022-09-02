from collections import deque
from turtle import st

class Solution:
    def findOrder(self, numCourses, prerequisites):
        adj = [[] for x in range(numCourses)]
        visited = [0 for x in range(numCourses)]
        for [course, prereq] in prerequisites:
            adj[prereq].append(course)
        
        topsort = []
        

        def dfs(startnode):
            visited[startnode] = 1
            for el in adj[startnode]:
                if visited[el] == 0:
                    if dfs(el):
                        return 1
                elif visited[el] == 1:
                    return 1
            topsort.append(startnode)
            visited[startnode] = 2
            

        for course in range(numCourses):
            if not visited[course]:
                if dfs(course):
                    return []
        
        return topsort[::-1]
        
sol = Solution()
# numCourses = 3
# prerequisites = [[0,1],[0,2],[1,2]]
# numCourses = 13
# prerequisites = [[2,0], [3,0], [4,3], [4,2], [2,1], [4,1], [5,1], [7,4], [6,4], [8,7], [8,6], [9,5], [10,5], [10,9], [12,10], [11,10], [10,6], [11,8]]
# numCourses = 4
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(sol.findOrder(numCourses, prerequisites))