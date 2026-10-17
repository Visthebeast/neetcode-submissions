import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*len(nums)
        for i in range(1,len(nums)):
            pref[i]=pref[i-1]*nums[i-1]
        
        suff = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            suff[i] = nums[i+1]*suff[i+1]
        res = []
        for i in range(len(nums)):
            res.append(pref[i]*suff[i])
        return res