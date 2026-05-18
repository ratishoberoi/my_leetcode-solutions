#TWO-POINTER

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width*h
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
    
#BRUTE FORCE 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        max_water = 0
        
        for i in range(n):
            for j in range(i+1, n):
                width = j - i
                water = width * min(height[i], height[j])
                if water > max_water:
                    max_water = water
        return max_water
    
    