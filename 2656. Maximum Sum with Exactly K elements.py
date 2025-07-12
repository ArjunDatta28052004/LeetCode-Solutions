class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        nums.sort()
        for i in range(k):
            max_sum += nums[-1]
            nums[-1] += 1
        return max_sum
        
