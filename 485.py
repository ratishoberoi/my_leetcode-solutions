class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_max=count=0
        for i in nums:
            if i == 1 :
                count+=1
                count_max=max(count,count_max)
            else:    
                count=0
        return count_max        