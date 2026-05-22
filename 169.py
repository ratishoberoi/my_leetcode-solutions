class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        max_freq=0
        majority=None
        for item in nums:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
            if freq[item]>max_freq:
                max_freq=freq[item]
                majority=item
        return majority                
    
    