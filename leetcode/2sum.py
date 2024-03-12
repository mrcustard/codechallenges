#!/usr/bin/env python3

class solution:
    def twoSum(self, nums, target):
        hm = {}

        for i in range(len(nums)):
            cp = target - nums[i]
            if cp in hm:
                return [hm[cp], i]
            hm[nums[i]] = i
        print(hm)






s = solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))
