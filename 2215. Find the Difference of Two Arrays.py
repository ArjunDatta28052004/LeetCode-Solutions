class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        result1 = list(nums1-nums2)
        answer.append(result1)
        result2 = list(nums2-nums1)
        answer.append(result2)
        return answer

        
