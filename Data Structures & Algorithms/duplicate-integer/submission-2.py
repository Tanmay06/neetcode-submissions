class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return not (len(nums) == len(set(nums)))

        for i in range(len(nums)):
            if nums[i] in nums[i + 1:]:
                return True
        return False

#  Time Complexity O(n) Space Complexity O(n)