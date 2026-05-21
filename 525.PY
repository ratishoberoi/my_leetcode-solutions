#TLE ERROR WALA BRUTE FORCE :

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            val = 1 if nums[i] == 1 else -1
            prefix[i+1] = prefix[i] + val   
        max_length = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if prefix[j] - prefix[i] == 0:
                    current_length = j - i
                    max_length = max(max_length, current_length)                   
        return max_length
    
#SET WALA ANS:

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_index_map = {0: -1}  
        current_sum = 0
        max_length = 0  
        for i in range(len(nums)):
            current_sum += 1 if nums[i] == 1 else -1
            if current_sum in sum_index_map:
                current_length = i - sum_index_map[current_sum]
                max_length = max(max_length, current_length)
            else:
                sum_index_map[current_sum] = i          
        return max_length    