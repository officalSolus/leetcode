class Solution:
    def reverse(self, x: int) -> int:
        y = ''.join(reversed(str(x)))
        if y[-1] == '-':
            y = y[:-1]
            ans = -1 * int(y)
        else:
            ans = int(y)

        if (-2)**31<= ans <= (2**31) - 1:
            return ans
        else:
            return 0
        
print(Solution().reverse(-123))