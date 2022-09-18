from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        S = [([],0)]
        while S:
            (comb, sum) = S.pop()
            if sum > target:
                continue
            if sum == target:
                result.append(comb)
                continue
            
            for el in candidates:
                if (comb and el >= comb[-1]) or not comb:
                    S.append((comb+[el],sum + el))
        return result

sol = Solution()
candidates = [2]
target = 3
print(sol.combinationSum(candidates, target))