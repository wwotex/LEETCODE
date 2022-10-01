from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1,-1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
                first = mid
                break
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1
                
        LAST = len(nums)-1
        left, right = 0, LAST
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target and (mid == LAST or nums[mid+1] > target):
                last = mid
                break
            elif target >= nums[mid]:
                left = mid+1
            else:
                right = mid-1
        return [first, last]
        