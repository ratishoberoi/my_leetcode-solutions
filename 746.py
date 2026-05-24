#TABULATION

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*(n+1)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n - 1], dp[n - 2])
    
#MEMORIZATION

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        n=len(cost)
        def dfs(i):
            if i<=1:
                return cost[i]
            if i in memo:
                return memo[i]
            memo[i]=cost[i] + min(dfs(i-1),dfs(i-2))
            return memo[i]
        return min(dfs(n-1),dfs(n-2))      