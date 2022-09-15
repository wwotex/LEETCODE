from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], new):
        ans = []
        for int in intervals:
            if int[1] < new[0]:
                ans.append(int)
            elif new[1] < int[0]:
                ans.append(new)
                new = int
            else:
                new[0] = min(new[0], int[0])
                new[1] = max(new[1], int[1])
        ans.append(new)
        return ans


# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval):
#         def overlaps(int1, int2):
#             return int1[0] <= int2[0] and int2[0] <= int1[1] or \
#                     int2[0] < int1[0] and int1[0] <= int2[1]

#         start = newInterval[0]
#         stop = newInterval[1]

#         i = 0
#         while i < len(intervals):
#             if overlaps(intervals[i], newInterval):
#                 start = min(start, intervals[i][0])
#                 stop = max(stop, intervals[i][1])
#                 intervals.pop(i)
#             else:
#                 i+=1
        
#         i = 0
#         while i < len(intervals) and intervals[i][0] < start:
#             i += 1
#         intervals.insert(i, [start, stop])
#         return intervals

sol = Solution()
intervals = [[1,5]]
newInterval = [1,7]
print(sol.insert(intervals, newInterval))