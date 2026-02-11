class Solution:
    def longestPalindrome(self, s: str) -> str:

        final = ''

        for x in range(len(s)):
            n = 1
            substr = s[x]

            while x-n >= 0 and x+n < len(s) and s[x-n] == s[x+n]:
                substr = s[x-n] + substr + s[x+n]
                n += 1

            if len(substr) > len(final):
                final = substr

            n = 0
            substr = ""

            while x-n >= 0 and x+1+n < len(s) and s[x-n] == s[x+1+n]:
                substr = s[x-n] + substr + s[x+1+n]
                n += 1

            if len(substr) > len(final):
                final = substr
        return final


