class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        for i in strs:
            if tuple(sorted(i)) in res_dict:
                res_dict[tuple(sorted(i))].append(i)
            else:
                res_dict[tuple(sorted(i))]=[i]
            
        return list(res_dict.values())