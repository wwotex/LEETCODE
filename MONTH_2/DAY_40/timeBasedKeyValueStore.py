from collections import defaultdict


class TimeMap:
    
    def __init__(self):
        self.D = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        print(f'obj.set("{key}","{value}",{timestamp})')
        self.D[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        print(f'obj.get("{key}",{timestamp})')
        arr = self.D[key]
        if not arr or timestamp < arr[0][0]: return ""
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + (right - left + 1) // 2
            if arr[mid][0] == timestamp: return arr[mid][1]
            
            if timestamp > arr[mid][0]:
                left = mid
            else:
                right = mid - 1
        return arr[left][1]


obj = TimeMap()
obj.set("love","high",10)
obj.set("love","low",20)
print(obj.get("love",5))
print(obj.get("love",10))
obj.get("love",15)
obj.get("love",20)
obj.get("love",25)