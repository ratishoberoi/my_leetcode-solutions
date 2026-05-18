# BRUTE FORCE 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
# TWO PASS HASHMAP :     

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            num_to_index[num] = i        
    
        for i, num in enumerate(nums):     
            complement = target - num
            if complement in num_to_index and num_to_index[complement] != i:
                return [i, num_to_index[complement]]
            
# ONE PASS HASHMAP :        

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:          
                return [num_to_index[complement], i]
            num_to_index[num] = i

# SORTING + 2 POINTERS :      

 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed = [(num, i) for i, num in enumerate(nums)]
        indexed.sort()                    
        
        left, right = 0, len(indexed) - 1
        
        while left < right:
            curr_sum = indexed[left][0] + indexed[right][0]
            
            if curr_sum == target:
                return [indexed[left][1], indexed[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1 

