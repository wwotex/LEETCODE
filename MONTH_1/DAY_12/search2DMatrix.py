class Solution:
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        def get(k):
            return matrix[k//m][k%m]

        left, right = 0, (n*m - 1)
        while left <= right:
            mid = (left + right) // 2
            # print(f'left: {get(left)}, mid: {get(mid)}, right: {get(right)}')
            el = get(mid)
            if el == target:
                return True
            elif target < el:
                right = mid - 1
            else:
                left = mid + 1

        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
sol = Solution()

for el in range(61):
    correct_answer = any(el in sublist for sublist in matrix)
    ans = "CORRECT" if (correct_answer) == (sol.searchMatrix(matrix, el)) else "WRONG"
    print(f'element: {el} {ans}')
print(sol.searchMatrix(matrix, target))