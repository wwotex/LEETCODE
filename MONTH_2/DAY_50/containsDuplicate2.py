from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        D = {}
        for i, el in enumerate(nums):
            if el in D and abs(i - D[el]) <= k:
                return True
            
            D[el] = i
        return False