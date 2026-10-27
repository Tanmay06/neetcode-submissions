class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            # diff = target - nums[i]
            # if diff in looked:
            #     return [looked[diff], i]
            # if nums[i] not in looked:
            #     looked[nums[i]] = i
            for i, val in enumerate(nums):
                if val in diff:
                    return [diff[val], i]
                else:
                    diff[target - val] = i