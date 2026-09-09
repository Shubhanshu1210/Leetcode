class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0:
                count=1
                el = num
            else:
                if el == num:
                    count+=1
                else:
                    count-=1
        count1=0
        for num in nums:
            if el == num:
                count1+=1
        if count1>len(nums)//2:
            return el
        return -1