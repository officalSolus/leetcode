class Solution:
    def intToRoman(self, num: int) -> str:
        ansl = [] 
        dupli = num
        place = 1
        syval = {0: '',1: 'I', 5: 'V',10: 'X', 50: 'L',100: 'C', 500: 'D', 1000: 'M' }
        

        while dupli != 0:
            n = dupli%10
            temp = 0
            if n==4:
                tempPlace = place*5
                temp = syval[place]+ syval[tempPlace]
                ansl.append(temp) 

            elif n == 9:
                tempPlace = place*10
                temp = syval[place]+ syval[tempPlace] 
                ansl.append(temp)

            elif n<4:
                ansl.append((syval[place]*n))
            elif n==5:
                ansl.append((syval[5*place]))
            elif n>5:
                temp = (syval[5*place]) + (syval[(int(place))]*(n-5))
                ansl.append(temp)
            dupli = int(dupli/10)
            place*=10
        ansl.reverse()
        ans = ''.join(ansl)
 
        return ans

        
#Better solution using greedy method.    

# class Solution:
#     def intToRoman(self, num: int) -> str:
#         values = [
#             (1000,"M"), (900,"CM"), (500,"D"), (400,"CD"),
#             (100,"C"), (90,"XC"), (50,"L"), (40,"XL"),
#             (10,"X"), (9,"IX"), (5,"V"), (4,"IV"), (1,"I")
#         ]

#         res = []

#         for v, s in values:
#             while num >= v:
#                 res.append(s)
#                 num -= v

#         return ''.join(res)


print(Solution().intToRoman(1994))