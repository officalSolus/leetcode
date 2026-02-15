class Solution:
    def threeSum(self, nums, d):
        sol = []
        n= len(nums)
        for x in range(0,n-2):
            i = x+1
            j= n-1
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            while i<j:

                tecsol = nums[i]+nums[x]+nums[j]
                z= [nums[i],nums[x],nums[j]]

                if tecsol==d:
                    sol.append(z)
                    while i<j and nums[i]==nums[i+1]:
                        i+=1
                    while i<j and nums[j]==nums[j-1]:
                        j-=1
                    j-=1
                    i+=1
                elif tecsol < d:
                    i+=1
                elif tecsol > d:
                    j-=1
        return sol


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        sol = []
        nums.sort()
        n = len(nums)

        for x in range(n - 3):

            if x > 0 and nums[x] == nums[x - 1]:
                continue

            rest = nums[x + 1:]

            triples = self.threeSum(rest,target - nums[x])

            for t in triples:
                sol.append([nums[x]] + t)

        return sol
    
nums = [1,0,-1,0,-2,2]

print(Solution().fourSum(nums,0))