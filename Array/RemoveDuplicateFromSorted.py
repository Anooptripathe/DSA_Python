class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        k=1
        i=1
        while i<len(nums):
            if nums[k-1]!=nums[i]:
                nums[k]=nums[i]
                k+=1
            i+=1
        return k