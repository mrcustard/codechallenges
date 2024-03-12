from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end:
                ans.append(nums[:])
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]


        ans = []
        backtrack(0, len(nums))
        return ans


s = Solution()
# test case 1
print(s.permute([1,2,3])) #== [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

# test case 2
#assert s.permute([0,1]) == [[0, 1], [1, 0]]

# test case 3
#assert s.permute([1]) == [[1]]

# Walkthrough
# [1,2,3]
# for i in range(0,3):
#  nums[0], nums[0] = nums[0], nums[0]
#  backtrack(0+1, 3)
#  nums[0], nums[0] = nums[0], nums[0]
