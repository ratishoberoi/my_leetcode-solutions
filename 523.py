class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1]=prefix[i]+nums[i]
            if prefix[i+1] % k ==0:
                return True
        return False        
    
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        for i in range(len(nums)):
            for j in range(i + 2, len(nums) + 1):
                subarray_sum = prefix[j] - prefix[i]
                if subarray_sum % k == 0:
                    return True
        return False

#TLE aa raha hai . Hashmap use karna hi padega ya Set use karna padega .         