from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ana = defaultdict(list)
        # for word in strs:
        #     ana[tuple(sorted(word))].append(word)

        # return list(ana.values())

        # Time O(nmlogm) n=len(nums) m=len(word)
        # Space O(nm)

        ana = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            ana[tuple(key)].append(word)
        
        return list(ana.values())