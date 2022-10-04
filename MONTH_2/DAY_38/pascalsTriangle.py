from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        for k in range(numRows-1):
            new_row = []
            for i in range(len(rows[-1])+1):
                new_row.append(0)
                new_row[i] += rows[-1][i-1] if i-1 >= 0 else 0
                new_row[i] += rows[-1][i] if i < len(rows[-1]) else 0
            rows.append(new_row)

        return rows

sol = Solution()
n = 5
print(sol.generate(n))