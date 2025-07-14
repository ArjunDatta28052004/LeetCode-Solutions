class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
            a = []
            i,j=0, 0
            while i<len(word1) and j<len(word2):
                a.append(word1[i])
                a.append(word2[j])
                i += 1
                j += 1
            
            a.append(word1[i:])
            a.append(word2[j:])
            return ''.join(map(str, a))

            
