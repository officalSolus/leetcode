class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        n= len(nums)
        nums.sort()
        for x in range(0,n):
            i = x+1
            j= n-1

            while i<j :
                tecsol = nums[i]+nums[x]+nums[j]
                if tecsol==0:
                    if [nums[i],nums[x],nums[j]] in sol or [nums[i],nums[j],nums[x]]in sol or
                    sol.append([nums[i],nums[x],nums[j]])
                elif tecsol < 0:
                    i+=1
                elif tecsol > 0:
                    j-=1


        return sol
    
    
Solution().threeSum([-1,0,1,2,-1,-4])