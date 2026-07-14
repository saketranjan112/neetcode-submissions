class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for st in strs:
            sorted_str = ''.join(sorted(st))
            if sorted_str in result:
                result[sorted_str].append(st)
            else:
                result[sorted_str] = [st]
        return list(result.values())