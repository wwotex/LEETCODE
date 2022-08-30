class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            l, m, r = nums[left], nums[mid], nums[right]
            
            # print(f'left: {l}, mid: {m}, right: {r}')

            if m == target:
                return mid
            elif (l < r and target < m or \
                (l > r and m > l and l <= target < m) or 
                (l > r and m < r and not m < target <= r)):
                right = mid - 1
            else:
                left = mid + 1

        return -1

nums = [4,5,6,7,8,1,2,3]
target = 3
sol = Solution()
print(sol.search(nums, target))

for el in range(-10, 10):
    correct_ans = nums.index(el) if el in nums else -1
    my_ans = sol.search(nums, el)
    print(f'element: {el} -> {"CORRECT" if correct_ans == my_ans else "WRONG"}')