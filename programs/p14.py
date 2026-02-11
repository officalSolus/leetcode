# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         ans = ''
#         if not strs:
#             return ""
        
#         if len(strs) == 1:
#             return strs[0]
#         if "" in strs:
#             return ""
#         s = strs[0]
#         i=1
#         j=1
#         while i<=len(s):
#             if j<len(strs):
#                 if s[0:i] == strs[j][0:i]:
#                     j+=1
#                 else:
#                     return ans
#             else:
#                 ans=s[0:i]
#                 i+=1
#                 j=1
#         return ans


#Better Solution

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""
            
        return prefix
    
print(Solution().longestCommonPrefix(["flower","flower","flower","flower"]))