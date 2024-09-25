class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        container = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            container = max(container, h * w)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return container