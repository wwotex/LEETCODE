from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline, result, H = [], [], [0]
        for [left, right, height] in buildings:
            skyline.append((left, height, 1))
            skyline.append((right, height, 0))
        skyline.sort()
        for i, (x, height, state) in enumerate(skyline):
            if state == 1:
                heappush(H, (-1)*height)
            else:
                H.remove((-1)*height)
                heapify(H)
            
            if (i+1 >= len(skyline) or skyline[i+1][0] != x) and (not result or result[-1][1] != H[0]*(-1)):
                result.append([x, (-1)*H[0]])
        return result

sol = Solution()
buildings = [[0,2,3],[2,5,3]]
print(sol.getSkyline(buildings))
