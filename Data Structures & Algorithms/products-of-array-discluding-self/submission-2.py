import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pref = [1]*n
        for i in range(1,n):
            pref[i]=pref[i-1]*nums[i-1]
        
        suff = [1]*n
        for i in range(n-2,-1,-1):
            suff[i] = nums[i+1]*suff[i+1]
        res = []
        for i in range(n):
            res.append(pref[i]*suff[i])
        return res