class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if len(nums)==1:
            return 0
        else:
            for i in range(len(nums)):
                pivot = i
                sum1 = sum(nums[:pivot])
                sum2 = sum(nums[pivot+1:])
                if(sum1==sum2):
                    return pivot
        return -1




        
