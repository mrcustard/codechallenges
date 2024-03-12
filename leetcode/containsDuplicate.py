from typing import List

class solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        if len(nums) == 0:
            return False

        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1

        for i, j in hm.items():
            if j > 1:
                return True
        return False

s = solution()
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

