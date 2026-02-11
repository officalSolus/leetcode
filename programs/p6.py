class Solution:
    def convert(self, s: str, numRows: int) -> str:
        l = {}
        x=0
        row = 0
        firstTime = True
        if len(s) <= numRows or numRows==1:
            pass
        else:
            while row!=numRows and firstTime:
                l[row] =list(s[x])
                x+=1
                row+=1
            firstTime = False
            

            while x!=len(s):
                row-=1
                while row!=0 and x!=len(s):
                    row-=1
                    l[row] += list(s[x])
                    x+=1
                row+=1
                while row!=numRows and x!=len(s):
                    l[row] +=s[x]
                    x+=1
                    row+=1
            l = list(l.values())
            l2 = []
            for x in l:
                l2.extend(x)
            s = ''
            for y in l2:
                s+=y

        return s
