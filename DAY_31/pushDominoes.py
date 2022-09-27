

from collections import deque


class Solution():
    def pushDominoes(self, dominoes):
        dominoes = list(dominoes)
        settimes = [0 for el in dominoes]
        Q = deque()
        for i, el in enumerate(dominoes):
            if el != '.': Q.appendleft(i)
        Q.appendleft(-1) # adding delimiter for time tracking
        timestep = 1
        while Q:
            curr = Q.pop()
            if curr == -1:
                if not Q: break
                timestep += 1
                Q.appendleft(-1)
                continue
            if dominoes[curr] == 'L' and curr > 0:
                if dominoes[curr-1] == '.':
                    dominoes[curr-1] = 'L'
                    Q.appendleft(curr-1)
                    settimes[curr-1] = timestep
                elif dominoes[curr-1] == 'R' and settimes[curr-1] == timestep:
                    dominoes[curr-1] = '.'
            if dominoes[curr] == 'R' and curr < len(dominoes)-1:
                if dominoes[curr+1] == '.':
                    dominoes[curr+1] = 'R'
                    Q.appendleft(curr+1)
                    settimes[curr+1] = timestep
                elif dominoes[curr+1] == 'L' and settimes[curr+1] == timestep:
                    dominoes[curr+1] = '.'

        return "".join(dominoes)

sol = Solution()
nums = '.L..R..L..'
print(sol.pushDominoes(nums))
