class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_group = defaultdict(list)

        for s in strs:
            sorted_key = ''.join(sorted(s))
            result_group[sorted_key].append(s)
        
        return list(result_group.values())




