class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums = nums2,nums1

        
        A,B = nums1, nums2
        m,n = len(A), len(B)

        low = 0
        high = m

        while low<=high:

            cutA = (low+high)//2
            cutB = (m+n+1)//2 - cutA


            leftA = float('-inf') if cutA==0 else A[cutA-1]
            leftB = float('-inf') if cutB==0 else B[cutB-1]

            rightA =  float('inf') if cutA==m else A[cutA]
            rightB = float('inf') if cutB ==n else B[cutB]

            if leftA <=rightB and leftB <= rightA:
                if (m+n)%2 ==0:
                    return (max(leftA,leftB) + min(rightA, rightB))/2
                else:
                    return max(leftA,leftB)
                

            elif leftA>rightB:
                high = cutA-1

            else:
                low= cutA+1