class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        ans = []
        for i in range(len(nums)):
            a = nums[i]
            more = target - a
            if more in mpp:
                ans.append(mpp[more])
                ans.append(i)
                return ans
            mpp[a]=i