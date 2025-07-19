
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums)) # sorts the actual array 
        return len(nums)
