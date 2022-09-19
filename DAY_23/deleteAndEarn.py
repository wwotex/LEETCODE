from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums = Counter(nums)
        S = [(0, nums)]
        ans = 0
        while S:
            (sum, curr) = S.pop()
            if len(curr) == 1:
                key = next(iter(curr))
                ans = max(ans, sum + key*curr[key])
                continue
            
            for key in curr.keys():
                new = curr.copy()
                new[key] -= 1
                if new[key] == 0: new.pop(key)
                if key+1 in new: new.pop(key+1)
                if key-1 in new: new.pop(key-1)
                if new:
                    S.append((sum+key, new))
                else:
                    ans = max(sum+key, ans)
        
        return ans

sol = Solution()

nums = [3,7,10,5,2,4,8,9,9,4,9,2,6,4,6,5,4,7,6,10]
print(sol.deleteAndEarn(nums))