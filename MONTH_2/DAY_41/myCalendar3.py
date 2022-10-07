from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.events = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.events[start] = self.events.get(start, 0) + 1
        self.events[end] = self.events.get(end, 0) - 1
        curr, max_k = 0, 0
        for el in self.events.values():
            curr += el
            max_k = max(max_k, curr)
        return max_k
        


obj = MyCalendarThree()
print(obj.book(10, 20))
print(obj.book(50, 60))
print(obj.book(10, 40))
print(obj.book(5, 15))
print(obj.book(5, 10))
print(obj.book(25, 55))
