
def sortColors(self, nums):
    lo,mid,high=0,0,len(nums)-1
    while(lo<=mid and mid<=high):
        if nums[mid]==0:
            nums[lo],nums[mid]=nums[mid],nums[lo]
            lo+=1
            mid+=1
        elif nums[mid]==2:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
        else:
            mid+=1
    return nums