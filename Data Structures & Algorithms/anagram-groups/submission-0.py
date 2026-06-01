class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for i in strs:
            new_i = ''.join(sorted(i))
            result[new_i].append(i)
        return list(result.values())