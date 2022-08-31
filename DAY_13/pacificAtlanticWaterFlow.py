from collections import deque
from this import d

class Solution:
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        ATLANTIC_MARKER, PACIFIC_MARKER, DOUBLE_MARKER = 1,2,3
        visited = [[0 for x in range(COLS)] for y in range(ROWS)]
        Q = deque()
        results = [] 
        def isAvailable(cell, prev, marker):
            return  0 <= cell[0] < ROWS and 0 <= cell[1] < COLS and \
                    heights[cell[0]][cell[1]] > heights[prev[0]][prev[1]] and \
                    visited[cell[0]][cell[1]] != marker and visited[cell[0]][cell[1]] != DOUBLE_MARKER

        def visitCell(cell, marker):
            if visited[cell[0]][cell[1]] == 0:
                visited[cell[0]][cell[1]] = marker 
            else: 
                visited[cell[0]][cell[1]] = DOUBLE_MARKER
                results.append([cell[0], cell[1]])
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            for dir in directions:
                new_x, new_y = cell[0] + dir[0], cell[1] + dir[1]
                if isAvailable((new_x, new_y), (cell[0], cell[1]), marker):
                    Q.append((new_x, new_y))

        #pacific (top-left)
        for el in range(ROWS):
            Q.append((el,0))
        for el in range(COLS):
            Q.append((0, el))
        
        while Q:
            cell = Q.pop()
            visitCell(cell, PACIFIC_MARKER)

        #atlantic (bot-right)
        for el in range(ROWS):
            Q.append((el, COLS-1))
        for el in range(COLS):
            Q.append((ROWS-1, el))
        
        while Q:
            cell = Q.pop()
            visitCell(cell, ATLANTIC_MARKER)



sol = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(sol.pacificAtlantic(heights))