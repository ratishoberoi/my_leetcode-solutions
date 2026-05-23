class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
        return count <= 1

class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        n = len(nums)
        for i in range(n):
            rotated = nums[i:] + nums[:i]
            if rotated == sorted_nums:
                return True
        return False
    
