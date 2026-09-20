class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n % 2 == 1:
            return float(nums[n // 2])
        else:
            m1 = nums[n // 2 -1]
            m2 = nums[n // 2]
            return (float(m1) + float(m2)) / 2.0