class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        n = len(s)
        count = sum(1 for i in s[:k] if i in vowels)
        max_count = count
        for i in range(k, n):
            if(s[i] in vowels):
                count += 1
            if(s[i-k] in vowels):
                count -= 1            
            max_count = max(max_count, count)
        return max_count


        
