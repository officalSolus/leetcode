class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        temp = x
        if x>=0:
            while temp!=0:
                z = temp%10
                rev = rev*10 +z
                temp = int(temp/10)
            if rev == x:
                return True
            else:
                return False
        else:
            return False
print(Solution().isPalindrome(121))