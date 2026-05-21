class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix= [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix[i+1]=prefix[i]+nums[i]
        for i in range(0,len(nums)):
            if prefix[i] == ( prefix[-1] - prefix[i+1] ):
                return i
        return -1        
