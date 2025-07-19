class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Compute prefix product
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Compute suffix product and multiply to result
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


        
