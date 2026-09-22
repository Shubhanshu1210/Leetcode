class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        pos = 0
        neg = 1
        for i in nums:
            if i < 0:
                ans[neg] = i
                neg += 2
            else:
                ans[pos] = i
                pos += 2
        return ans