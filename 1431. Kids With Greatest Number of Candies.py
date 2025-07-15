class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a = []
        maximum = max(candies)
        for i in candies:
            if(i+extraCandies>=maximum):
                a.append(True)
            else:
                a.append(False)
        return a
        
