class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums = sorted(nums)
        left, right = 0, len(nums)-1
        while left<right:
            total = nums[left] + nums[right]
            if total == k:
                count += 1
                left += 1
                right -= 1
            elif total<k:
                left += 1
            else:
                right -= 1
        return count
            
