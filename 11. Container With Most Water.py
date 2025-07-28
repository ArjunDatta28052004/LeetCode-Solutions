class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        max_area = min(height[left], height[right]) * (right-left)
        while(left<right):
            if(height[left]<height[right]):
                left+=1
            elif(height[left]>height[right]):
                right -= 1
            else:
                left += 1
                right -= 1
            new_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, new_area)
        return max_area
