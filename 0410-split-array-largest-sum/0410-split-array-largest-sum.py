class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)

        while l < r:
            mid = (l + r) // 2

            subarrays = 1
            current_sum = 0

            for num in nums:
                if current_sum + num > mid:
                    subarrays += 1
                    current_sum = num
                else:
                    current_sum += num

            if subarrays <= k:
                r = mid
            else:
                l = mid + 1

        return l