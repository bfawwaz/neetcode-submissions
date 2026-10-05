class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, x in enumerate(nums):
            y = target - x
            if y in seen:
                return [seen[y], index]
            seen[x] = index