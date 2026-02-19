class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def recurs(curr, openx,closex):
            if len(curr) == 2*n:
                ans.append(curr)
                return
            
            if openx < n:
                recurs(curr+ "(" ,openx+1, closex)
            
            if openx>closex:
                recurs(curr+")", openx,closex+1)

        recurs("",0,0)            
        return ans
