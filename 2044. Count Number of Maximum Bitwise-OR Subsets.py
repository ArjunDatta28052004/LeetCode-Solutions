from itertools import combinations
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_bitwise =0
        for i in range(len(nums)):
            max_bitwise = max_bitwise | nums[i]
        count = 0
        subsets = []
        for i in range(len(nums)+1):
            subsets.extend(combinations(nums, i))
        for i in range(len(subsets)):
            bitwise = 0
            for j in subsets[i]:
                bitwise = bitwise | j
            if(bitwise==max_bitwise):
                count += 1
        return count

            


