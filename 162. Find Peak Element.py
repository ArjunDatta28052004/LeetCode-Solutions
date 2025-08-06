class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        high = len(nums) - 1
        low = 0
        while low<high:
            mid = (low+high)//2
            if nums[mid] > nums[mid+1]:
                high = mid
            else:
                low = mid+1
        return low
