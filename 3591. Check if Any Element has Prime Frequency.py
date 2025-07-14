class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,31, 37, 41, 43, 47, 53, 59, 61, 67,  71, 73, 79, 83, 89, 97, 101,103,107]
        for i in nums:
            if(nums.count(i) in a):
                return True
                break
            
        return False
        
