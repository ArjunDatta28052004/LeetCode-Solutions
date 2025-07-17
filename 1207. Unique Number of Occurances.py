class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = set(arr)
        occur = []
        for i in a:
            occur.append(arr.count(i))
        x = 0
        for i in range(len(occur)-1):
            for j in range(i+1, len(occur)):
                if(occur[i]==occur[j]):
                    return False
        return True
