class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        n=len(nums)
        m=[]
        for item in nums:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
        for i in range(k):
            max_key=max(freq,key=freq.get)
            m.append(max_key)
            freq[max_key]=0
        return m                 