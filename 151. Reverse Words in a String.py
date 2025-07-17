class Solution:
    def reverseWords(self, s: str) -> str:
        s = " ".join(s.split())
        s = s.split(" ")
        s=s[::-1]
        return " ".join(s)
        
