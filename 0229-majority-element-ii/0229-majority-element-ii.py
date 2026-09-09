class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lis = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num]>len(nums)/3:
                if num not in lis:
                    lis.append(num)
                
        return lis