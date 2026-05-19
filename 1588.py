class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum=[0] * (len(arr)+1)
        total_sum=0
        for i in range(len(arr)):
            prefix_sum[i+1]=prefix_sum[i]+arr[i]
        for i in range(len(arr)):
            for j in range (i,len(arr)):
                if len(arr[i:j+1]) % 2 !=0:
                    total_sum+=(prefix_sum[j+1]-prefix_sum[i])
        return total_sum            