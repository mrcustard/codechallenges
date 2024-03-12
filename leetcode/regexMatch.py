#!/usr/bin/env python3

import enum

class solution:
    def isMatch(self, s: str, p: str) -> bool:
        # . matches a single character
        # * matches zero or more of the preceding element
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
            else:
                fm = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j+1] == '*':
                    ans = dp(i, j+2) or fm and dp(i+1, j)
                else:
                    ans = fm and dp(i+1, j+1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)


s = solution()

s.isMatch('aa', 'a')
s.isMatch('aa', '*')
s.isMatch('aa', '.')
