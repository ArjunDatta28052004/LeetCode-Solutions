class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        ans = []
        for i in range(len(s)):
            if(s[i]!='*'):
                ans.append(s[i])
            else:
                ans.pop()
        return ''.join(ans)
            


             
