class Solution(object):
    def twoSum(self, nums, target):
        lst = []
        for i in range(len(nums)+1):
            for j in range(i):
                if nums[i]+nums[j]==target:
                    lst.append(i)
                    lst.append(j)
                    return lst
                else:
                    j += 1
