class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = []
        for el in nums:
            if len(curr_sum) > 0:
                curr_sum.append( curr_sum[-1] + el)
            else:
                curr_sum.append( el )
        
        return curr_sum