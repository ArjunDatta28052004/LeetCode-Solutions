class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        a = []
        s = list(s)
        for i in range(len(s)):
            if(s[i] in vowels):
                a.append(s[i])
        for i in range(len(s)):
            if(s[i] in vowels):
                s[i] = a[-1]
                a.pop()
        return ''.join(s)
