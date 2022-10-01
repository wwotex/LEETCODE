import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq._heapify_max(stones)
            y = heapq._heappop_max(stones)
            x = heapq._heappop_max(stones)
            if x != y:
                heapq.heappush(stones, y-x)
            
        if stones:
            return stones[0]
        else:
            return 0
        

sol = Solution()
stones = [2,7,4,1,8,1]
print(sol.lastStoneWeight(stones))