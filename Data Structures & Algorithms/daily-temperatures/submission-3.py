class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # # Brute Force Time O(n^2) Space O(1)
        # res = []
        # n = len(temperatures)
        # for i in range(n):
        #     count = 1
        #     j = i + 1
        #     while j < n:
        #         if temperatures[j] > temperatures[i]:
        #             break
        #         count += 1
        #         j += 1
        #     count = 0 if j == n else count
        #     res.append(count)
        # return res

        # Stack Time O(n) Space O(n)
        res = [0] * len(temperatures)
        stack = []

        for i, val in enumerate(temperatures):
            if stack:
                while stack and stack[-1][0] < val:
                    res[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
            stack.append((val, i))
        
        return res

