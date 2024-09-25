class Solution:
    def maxArea(self, height: list[int]) -> int:
        container = 0
        i = 0
        while i < len(height)-1:
            j = i+1
            while j < len(height):
                dist = j-i
                water = dist * min(height[i],height[j])
                if water > container:
                    container = water
                j+=1
            i +=1
        return container