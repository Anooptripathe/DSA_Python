class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,j,n=0,0,len(nums)
        while i<=j and j<n:
            if nums[j]!=0:
                nums[i]=nums[j]
                i+=1
            j+=1

        while i<=n-1:
            nums[i]=0
            i+=1