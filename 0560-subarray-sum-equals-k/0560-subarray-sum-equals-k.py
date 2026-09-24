class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mpp = {}
        mpp[0] = 1
        count = 0
        presum = 0
        for i in range(len(nums)):
            presum = presum + nums[i]
            remove = presum - k
            count += mpp.get(remove, 0)
            mpp[presum] = mpp.get(presum, 0) + 1
        return count
