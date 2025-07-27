class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        arr = [nums[0]]
        for i in range(1, n):
            if(nums[i]!=nums[i-1]):
                arr.append(nums[i])
        for i in range(1,len(arr)-1):
            if((arr[i-1]<arr[i] and arr[i]>arr[i+1]) or (arr[i-1]>arr[i] and arr[i+1]>arr[i])):
                count += 1
        return count
