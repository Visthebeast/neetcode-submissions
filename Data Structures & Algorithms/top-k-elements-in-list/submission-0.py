from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resl = Counter(nums)

        r = [i for i,j in resl.most_common(k)]
        return r