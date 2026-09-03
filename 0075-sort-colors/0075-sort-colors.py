class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a=0
        b=0
        c=0
        for num in nums:
            if num==0:
                a=a+1
            if num==1:
                b=b+1
            if num==2:
                c=c+1
        for i in range(a):
            nums[i]=0
        for i in range(a,a+b,1):
            nums[i]=1
        for i in range(a+b,a+b+c,1):
            nums[i]=2

        