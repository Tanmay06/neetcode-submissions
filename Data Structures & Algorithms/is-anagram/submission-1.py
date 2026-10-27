# from collections import Counter
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count_s = Counter(s)
        # count_t = Counter(t)
        # return count_s == count_t
        count_s = defaultdict(int)
        for i in s:
            count_s[i] += 1
        
        count_t = defaultdict(int)
        for i in t:
            count_t[i] += 1
        
        return count_s == count_t

        # Time O(n)
        # Space O(n)