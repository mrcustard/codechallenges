from typing import List

class solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        m = {}
        for i,num in enumerate(nums):
            if num in m:
                if m[num][0][1] > 1:
                  m[num][0] = (i, m[num][0][1])
                else:
                  m[num][0] = (m[num][0][0], i)
                  m[num] = [m[num][0], m[num][1] + 1]

            else:
                m[num] = [(i, 0), 1]

        for i, j in m.items():

            if j[1] >= 1:
                if j[0][0] != j[0][1] and abs(j[0][0] - j[0][1]) <= indexDiff and abs(nums[j[0][0]] - nums[j[0][1]]) <= valueDiff:
                    return True
            return False





s = solution()

assert s.containsNearbyAlmostDuplicate([1,2,3,1],3,0) == True
assert s.containsNearbyAlmostDuplicate([1,0,1,1],1,2) == True
assert s.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3) == False
assert s.containsNearbyAlmostDuplicate([8,7,15,1,6,1,9,15],1,3) == True