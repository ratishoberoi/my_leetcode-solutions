#TABULATION

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def robLinear(arr):
            m = len(arr)
            if m == 1:
                return arr[0]
            dp = [0] * m
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            for i in range(2, m):
                dp[i] = max(arr[i] + dp[i-2],dp[i-1])
            return dp[m-1]
        return max(robLinear(nums[:-1]),robLinear(nums[1:]))
    
#MEMORIZATION

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def robLinear(arr):
            memo = {}
            def dfs(i):
                if i < 0:
                    return 0
                if i == 0:
                    return arr[0]
                if i in memo:
                    return memo[i]
                memo[i] = max(arr[i] + dfs(i - 2),dfs(i - 1))
                return memo[i]
            return dfs(len(arr) - 1)
        return max(robLinear(nums[:-1]),robLinear(nums[1:]))    