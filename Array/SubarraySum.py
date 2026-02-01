class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pref_sum=0
        cnt=0
        count_map={0:1}

        for i in range(0,len(nums)):
            pref_sum+=nums[i]
            if (pref_sum-k) in count_map:
                cnt+=count_map[pref_sum-k]
            count_map[pref_sum]=count_map.get(pref_sum,0)+1

        return cnt

