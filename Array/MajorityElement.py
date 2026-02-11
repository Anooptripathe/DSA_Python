def majorityElement(self, nums):
        cnt,maxm=1,nums[0]
        for i in range(1,len(nums)):
            if maxm==nums[i]:
                cnt+=1
            else:
                cnt-=1
            if cnt<0:
                maxm=nums[i]
                cnt+=1
        return maxm