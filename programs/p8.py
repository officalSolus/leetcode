class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 0
        ans= 0
        digitFound = False
        letterFound = False
        signUsed = False

        prev = ''
        for x in s:
            if x==" " and digitFound == False and not signUsed: 
                pass
            elif (x == '+' or x == '-') and not digitFound and not signUsed:
                signUsed = True
                if x == '-':
                    sign = 1
            elif digitFound == True:
                try:
                    z = int(x)
                    ans =ans*10+z
                except:
                    break
            elif digitFound == False:
                try:
                    z = int(x)
                    ans =ans*10+z
                    digitFound = True
                except:
                    letterFound = True
                    break
            prev = x
        if sign == 1:
            ans = -1*ans
        
        if -2**31<= ans <=2**31 - 1:
            return ans
        else:
            if str(ans)[0] == '-':
                return -2**31
            else:
                return 2**31 -1 
    