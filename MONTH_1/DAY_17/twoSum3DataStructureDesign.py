from collections import defaultdict

class TwoSum:
    def __init__(self):
        self.nums = []
        self.D = defaultdict(int)

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.D[number] += 1

    def find(self, value: int) -> bool:
        for el in self.nums:
            if value - el == el:
                if self.D[el] > 1:
                    return True
            elif value - el in self.D:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)