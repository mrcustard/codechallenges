class Solution:
    def atoi(self, s: str) -> int:
        s = s.strip() # strip whitespace
        sign = ""

        if s.startswith('-'):
            sign = "-"
            s = s.strip('-')
        else:
            sign = "+"
            s = s.strip('+')

        number = int(s)
        if number.bit_length() > 32:
            return 0
        else:
            return number

s = Solution()
print(s.atoi('-123'))
