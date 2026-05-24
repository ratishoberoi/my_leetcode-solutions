#TABULATION

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)
    
#MEMORIZATION

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            best = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    best = max(
                        best,
                        dfs(j) + 1
                    )
            memo[i] = best
            return best
        ans = 0
        for i in range(len(nums)):
            ans = max(
                ans,
                dfs(i)
            )
        return ans    