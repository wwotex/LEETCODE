from typing import List


class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        p1, p2 = 0, 0 
        result = []
        while p1 < len(first) and p2 < len(second):
            open = max(first[p1][0], second[p2][0])
            close = min(first[p1][1], second[p2][1])
            
            if open <= close:
                result.append([open,close])

            if first[p1][1] < second[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return result

# class Solution:
#     def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
#         p1, p2 = 0, 0 
#         result = []
#         while p1 < len(first) and p2 < len(second):
#             open = first[p1][0] if second[p2][0] < first[p1][0] else second[p2][0]
#             (close, firstClosed) = (first[p1][1], True) if first[p1][1] < second[p2][1] else (second[p2][1], False)
            
#             if open <= close:
#                 result.append([open, close])
            
#             if firstClosed:
#                 p1 += 1
#             else:
#                 p2 += 1
#         return result

# class Solution:
#     def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
#         p1, p2 = 0, 0 
#         result = []
#         open = None
#         while p1 < len(first) and p2 < len(second):
#             if first[p1][0] < second[p2][0]:
#                 if first[p1][1] < second[p2][0]:
#                     p1 += 1
#                 elif first[p1][1] < second[p2][1]:
#                     result.append([second[p2][0], first[p1][1]])
#                     p1 += 1
#                 else:
#                     result.append([second[p2][0], second[p2][1]])
#                     p2 += 1
#             else:
#                 if second[p2][1] < first[p1][0]:
#                     p2 += 1
#                 elif second[p2][1] < first[p1][1]:
#                     result.append([first[p1][0], second[p2][1]])
#                     p2 += 1
#                 else:
#                     result.append([first[p1][0], first[p1][1]])
#                     p1 += 1
#         return result

sol = Solution()
firstList = [[1,3],[5,9]]
secondList = []
print(sol.intervalIntersection(firstList, secondList))
print([[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])

