#TABULATION
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+1)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp[0]=nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(nums[i] + dp[i-2],dp[i-1])
        return dp[n-1]    
    
#MEMORIZATION

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        if n == 0: return 0
        if n == 1: return nums[0]
        def dfs(i):
            if i < 0: return 0
            if i == 0: return nums[0]
            if i in memo: return memo[i]
            memo[i] = max(nums[i] + dfs(i - 2), dfs(i - 1))
            return memo[i]
        return dfs(n - 1)    