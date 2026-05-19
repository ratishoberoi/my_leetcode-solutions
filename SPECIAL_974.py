class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum=[0] * (len(nums)+1)
        total_sum=0
        count=0
        for i in range(len(nums)):
            prefix_sum[i+1]=prefix_sum[i]+nums[i]
        for i in range(len(nums)):
            for j in range (i,len(nums)):
                if (prefix_sum[j+1]-prefix_sum[i]) % k == 0 :
                    count+=1
        return count        
    
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        count = 0
        remainder_counts = {}  
        for val in prefix_sum:
            rem = val % k
            if rem < 0:
                rem += k
            if rem in remainder_counts:
                count += remainder_counts[rem]
                remainder_counts[rem] += 1
            else:
                remainder_counts[rem] = 1
                
        return count    