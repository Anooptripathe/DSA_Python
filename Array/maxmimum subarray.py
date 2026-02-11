class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot=-100009
        sum,i=0,0
        while i<len(nums):
            sum+=nums[i]
            tot=max(tot,sum)
            if sum<0:
                sum=0
            i+=1
        return tot
        
        
