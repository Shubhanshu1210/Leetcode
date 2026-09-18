class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        length = 0
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                length += 1
                maxlen = max(length, maxlen)
            else:
                length = 0
            
        return maxlen