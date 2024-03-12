class Solution:
    def isPalendrome(self, s) -> bool:
        s = [i for i in s.lower() if i.isalnum()]
        return s == s[::-1]



s = Solution()
print(s.isPalendrome("A man, a plan, a canal: Panama"))