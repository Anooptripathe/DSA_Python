class Solution:
    def secondLargestElement(self, nums):
        largest=nums[0]
        second_largest=float('-inf')
        for i in range(1,len(nums)):
            if nums[i]>largest:
                second_largest=largest
                largest=nums[i]
                
            elif nums[i]>second_largest and nums[i]!=largest:
                second_largest=nums[i]
        if second_largest==float('-inf'):
            return -1
        else:
            return second_largest