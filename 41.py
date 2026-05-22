class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        target = 1
        for num in nums:
            if num == target:
                target += 1
        return target
    
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        for i in range(1, n + 2):
            if i not in num_set:
                return i    