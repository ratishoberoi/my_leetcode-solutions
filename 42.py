class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0
        for i in range(1, n - 1):
            left_max = max(height[:i+1])
            right_max = max(height[i:])  
            total_water += min(left_max, right_max) - height[i]
        return total_water
    
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        total_water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1
        return total_water    