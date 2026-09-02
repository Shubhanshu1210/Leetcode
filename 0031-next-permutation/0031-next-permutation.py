class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        ind = -1
        temp = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind = i
                break
        if ind == -1:
            nums.reverse()
        else:
            for i in range(len(nums)-1,ind,-1):
                if nums[i]>nums[ind]:
                    temp = nums[i]
                    nums[i] = nums[ind]
                    nums[ind] = temp
                    break
            nums[ind+1:] = reversed(nums[ind+1:])
            

        