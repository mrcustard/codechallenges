from typing import List

class solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if not nums or indexDiff <= 0 or valueDiff < 0:
            return False

        mini = min(nums)
        diff = valueDiff + 1
        bucket = {}

        def getKey(num: int) -> int:
            return (num - mini) // diff

        for i, num in enumerate(nums):
            key = getKey(num)
            if key in bucket:
                return True
            # Left adjacent bucket
            if key - 1 in bucket and num - bucket[key - 1] < diff:
                return True
            if key + 1 in bucket and bucket[key + 1] - num < diff:
                return True
            bucket[key] = num
            if i >= indexDiff:
                del bucket[getKey(nums[i - indexDiff])]
        return False





s = solution()

assert s.containsNearbyAlmostDuplicate([1,2,3,1],3,0) == True
assert s.containsNearbyAlmostDuplicate([1,0,1,1],1,2) == True
assert s.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3) == False
assert s.containsNearbyAlmostDuplicate([8,7,15,1,6,1,9,15],1,3) == True