class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        print(nums)
        j=1
        res=0
        for i in range(1,len(nums)):
            d=nums[i]-nums[i-1]
            print(d)
            if not d:
                # print("skipping")
                continue
            if d>1:
                # print("inside:",j)
                if j>res:
                    res=j
                j=1
            else:
                # print("j:",j)
                j+=1
        if j>res:
            res=j
        
        return res
