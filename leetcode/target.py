class findTarget:
    def __init__(self):
        self.hashmap = {}
        self.index = 0

    def targ(self, nums, target):
        for i, num in enumerate(nums):
            comp = target - num
            if comp  in self.hashmap:
                return [self.hashmap[comp], i]
            self.hashmap[num] = i
        return []





f = findTarget()
print(f.targ([1,2,4], 3))
print(f.targ([3,2,4], 6))

