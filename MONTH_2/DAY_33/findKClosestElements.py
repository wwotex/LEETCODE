from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)-k
        while left < right: 
            mid = (right + left)//2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid+1
            else:
                right = mid
        return arr[left:left+k]

# class Solution:
#     def findClosestElements(self, arr: List[int],  k: int, x: int) -> List[int]:
#         left, mid, right = 0, 0, len(arr)-1
#         while left < right: 
#             mid = (right + left)//2
#             if arr[mid] == x: break
#             if x > arr[mid]:
#                 left = mid+1
#             else:
#                 right = mid
#         mid = (right + left)//2
#         (left, right) = (mid, mid+1) if arr[mid] < x else (mid-1, mid)
#         result = []
#         for i in range(k):
#             if right >= len(arr) or abs(arr[left]-x) <= abs(arr[right]-x):
#                 temp = arr[left]
#                 left -= 1
#             else:
#                 temp = arr[right]
#                 right += 1
#             result.append(temp)

#         result.sort()
#         return result

sol = Solution()
nums = [4,5,7,9,15]
k = 5
for el in range(0, 20):
    print(f'{el} -> {sol.findClosestElements(nums, k, el)}' )