#BRUTE FORCE : 

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums or target <= nums[0]:
            return 0
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            if nums[i] < target and (i + 1 == len(nums) or nums[i+1] > target):
                return i+1    
            
#BINARY SEARCH

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left            