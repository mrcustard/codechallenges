
class solution:
    def isInterleave(self, s1, s2, s3):
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)

        if s1_len + s2_len != s3_len:
            return False
        dp = [[False] * (s2_len + 1) for _ in range(s1_len + 1)]
        dp[0][0] = True


s = solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(s.isInterleave("aabcc", "dbbca", "aadbbaccc"))