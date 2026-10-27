from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            ana[sorted_word].append(word)

        return list(ana.values())

# Time O(nm) n=len(nums) m=len(word)
# Space O(nm)