class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        maxV = 0
        while i<j:
            mV = (j-i)*min(height[i],height[j])
            
            if mV>maxV:
                maxV= mV

            if height[i]>height[j]:
                j-=1
            elif height[i] < height[j]:
                i+=1
            else:
                i+=1
                j-=1
        return maxV
            