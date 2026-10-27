from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freqs = []
        for i in counts:
            freqs.append((counts[i], i))
        freqs.sort()
        return [val[1] for val in freqs[len(freqs) - k:]]