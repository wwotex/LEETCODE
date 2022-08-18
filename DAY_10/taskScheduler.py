class Solution:
    def leastInterval(self, tasks, n):
        dtasks = {}
        for el in tasks:
            if el not in dtasks:
                dtasks[el] = 1
            else:
                dtasks[el] += 1
        index = 0
        occurences = [0 for x in range(n)]
        while dtasks:
            x = index
            for task in dtasks:
                if task not in occurences:
                    index += 1
                    occurences.append(task)
                    if len(occurences) > n:
                        occurences.pop(0)
                    dtasks[task] -= 1
                    if dtasks[task] == 0:
                        dtasks.pop(task)
                    break
            if index == x:
                index += 1
                occurences.append(0)
                if len(occurences) > n:
                        occurences.pop(0)
        return index

sol = Solution()

tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n = 2
print(sol.leastInterval(tasks, n))