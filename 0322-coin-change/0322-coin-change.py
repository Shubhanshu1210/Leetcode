class Solution:
    def f(self, index, T, nums, dp):
        if dp[index][T] != -1:
                return dp[index][T]
        if(index == 0):
            if T % nums[0] == 0:
                return T // nums[0]
            return 1e9
            if dp[index][T] != -1:
                return dp[index][T]
        nottake = 0 + self.f(index-1, T, nums, dp)
        take = float('inf')
        if nums[index] <= T:
            take = 1 + self.f(index, T-nums[index], nums, dp)
        dp[index][T] = min(take, nottake)
        return dp[index][T]
        
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        ans = self.f(len(coins)-1, amount, coins, dp)
        if(ans >= 1e9):
            return -1
        return ans