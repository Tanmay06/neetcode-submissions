from collections import defaultdict

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # # Time O(n^2) Space O(1) iteration for every element
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]



        # # Time O(nlogn) Space O(1) Binary search
        # for i in range(len(numbers)):
        #     l = i + 1
        #     r = len(numbers) - 1
        #     diff = target - numbers[i]
        #     while l <= r:
        #         mid = l + (r - l) // 2
        #         if numbers[mid] == diff:
        #             return [i + 1, mid + 1]
        #         elif numbers[mid] < diff:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        # return []


        # Time O(n) Space O(n) hasMap
        track = defaultdict(int)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            # print(track)
            if track[diff] :
                return [track[diff], i + 1]
            track[numbers[i]] = i + 1
        return []

