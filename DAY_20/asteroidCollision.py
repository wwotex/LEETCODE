import ast
from turtle import right
from typing import AsyncIterable, List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        rightGoingStack = []
        leftGoingList = []
        for ast in asteroids:
            if ast < 0:
                if not rightGoingStack:
                    leftGoingList.append(ast)
                else:
                    while rightGoingStack and rightGoingStack[-1] < (-ast):
                        rightGoingStack.pop()
                    if not rightGoingStack:
                        leftGoingList.append(ast)
                    elif rightGoingStack[-1] == (-ast):
                        rightGoingStack.pop()
            else:
                rightGoingStack.append(ast)
        return leftGoingList + rightGoingStack
                
sol = Solution()
asteroids = [-2,-1,1,2]
print(sol.asteroidCollision(asteroids))