class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        n=len(nums)
        m=[]
        for item in nums:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
            if freq[item]>n//3:
                if item not in m:
                    m.append(item)
        return m                    
