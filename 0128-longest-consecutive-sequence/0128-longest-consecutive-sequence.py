class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0 :
            return 0
        nums.sort()
        n = len(nums)
        LS = float('-inf')
        count = 0
        longest = 1
        for i in nums:
            if i-1 == LS:
                count+=1
                LS = i
            elif LS != i:
                count = 1
                LS = i
            longest = max(longest,count)
        return longest
            