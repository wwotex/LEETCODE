import operator
from typing import List


def searchFirst(nums: List[int], target: int):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
            return mid
        elif target > nums[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1
        
def searchLast(nums: List[int], target: int):
    LAST = len(nums)-1
    left, right = 0, LAST
    while left <= right:
        mid = left + (right-left)//2
        if nums[mid] == target and (mid == LAST or nums[mid+1] > target):
            return mid
        elif target >= nums[mid]:
            left = mid+1
        else:
            right = mid-1
    return -1
    
def lastIndex(lst, value):
    return len(lst) - operator.indexOf(reversed(lst), value) - 1

nums = [2,2]
for target in range(5):
    if target not in nums:
        if searchLast(nums,target) != -1:
            print(f'error: {target}')
    elif searchLast(nums,target) != lastIndex(nums, target):
        print(f'error: {target}')
        
