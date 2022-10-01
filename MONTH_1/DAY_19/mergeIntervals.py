from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for i, int in enumerate(intervals):
            if i == 0 or int[0] > ans[-1][1]:
                ans.append(int)
            else:
                ans[-1][1] = max(ans[-1][1], int[1])
        return ans