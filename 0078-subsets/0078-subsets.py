class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        totalSubsets = 1 << n
        ans = []
        for val in range(totalSubsets):
            subset = []
            for i in range(n):
                
                if val & (1 << i):
                    subset.append(nums[i])

            ans.append(subset)

        return ans