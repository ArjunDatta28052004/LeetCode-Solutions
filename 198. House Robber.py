class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        a = [0] * n
        a[0] = nums[0]
        a[1] = max(nums[0], nums[1])
        for i in range(2, n):
            a[i] = max(a[i-1], nums[i]+a[i-2])
        return a[-1]
        
