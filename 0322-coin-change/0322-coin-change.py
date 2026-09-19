class Solution:
    def f(self, index, T, coins, dp):
        if dp[index][T] != -1:
                return dp[index][T]
        if(index == 0):
            if T % coins[0] == 0:
                return T // coins[0]
            return 1e9
            if dp[index][T] != -1:
                return dp[index][T]
        nottake = 0 + self.f(index-1, T, coins, dp)
        take = float('inf')
        if coins[index] <= T:
            take = 1 + self.f(index, T-coins[index], coins, dp)
        dp[index][T] = min(take, nottake)
        return dp[index][T]
        
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        for i in range(amount+1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = 1e9
        for index in range(1,len(coins)):
            for T in range(amount+1):
                nottake = 0 + dp[index - 1][T]
                take = float('inf')
                if coins[index] <= T:
                    take = 1 + dp[index][T-coins[index]]
                dp[index][T] = min(take, nottake)
                
                
        ans = dp[len(coins)-1][amount]
        if(ans >= 1e9):
            return -1
        return ans