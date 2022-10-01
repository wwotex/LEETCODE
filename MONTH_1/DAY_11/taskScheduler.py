import heapq
from typing import Counter


class Solution:
    def leastInterval(self, tasks, n):
        tasks_count = Counter(tasks)
        task_heap = [-cnt for cnt in tasks_count.values()]
        heapq.heapify(task_heap)
        Q = []
        cycle = 0
        while task_heap or Q:
            if Q and Q[0][1] == cycle:
                temp = Q.pop(0)
                heapq.heappush(task_heap, temp[0])
            if task_heap:
                task = heapq.heappop(task_heap)
                task += 1
                if task != 0:
                    Q.append((task, cycle + n + 1))
            cycle += 1
            
        return cycle
                


sol = Solution()

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(sol.leastInterval(tasks, n))