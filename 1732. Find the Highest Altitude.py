class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a=[]
        a.append(0)
        maxi = a[0]
        for i in range(0,len(gain)):
            maxi += gain[i]
            a.append(maxi)
        return max(a)
        
