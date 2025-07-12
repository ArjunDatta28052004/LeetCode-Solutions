class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        median = 0.0
        if(len(nums1)%2!=0):

            mid = int((0+(len(nums1)-1))/2)
            median = nums1[mid]
        else:
            mid1 = int((len(nums1)-1)/2)
            median = (nums1[mid1]+nums1[mid1+1])/2
        return median
