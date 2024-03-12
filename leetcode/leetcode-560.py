# Given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: nums = [1,1,1], k = 2
# Output: 2
#
# Example 2:
#
# Input: nums = [1,2,3], k = 3
# Output: 2

from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumCount = defaultdict(int)
        count = 0
        currentSum = 0

        for i in nums:
            # calculate sum until current number
            currentSum += i

            # check if we have seen a number that could be subtracted
            # from the current value to equal k. Add number of occurrences of x to counter
            count += sumCount[currentSum - k]
            # update sum counter
            sumCount[currentSum] += 1
        # check if any of the sums from the first to any other position match k
        count += sumCount[k]
        # return the count
        return count





s = Solution()
assert s.subarraySum([1,1,1], 2) == 2
assert s.subarraySum([1,2,3], 3) == 2
