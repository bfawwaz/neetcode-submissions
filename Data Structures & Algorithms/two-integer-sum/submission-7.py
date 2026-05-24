class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = len(nums)-1
        i = 0
        if nums[i] + nums[j] == target:
            return [i,j]
        while j>=0:
            if j == i:
                j = len(nums) - 1
                i = i + 1
            if nums[i] + nums[j] == target:
                return [i,j]
            j = j-1