class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = []
        for i, num in enumerate(nums):
            history.append([num,i])
        history.sort()
        i = 0
        j = len(nums)-1
        while i < j:
            current = history[i][0] + history[j][0]
            if current == target:
                return [min(history[i][1], history[j][1]),
                        max(history[i][1], history[j][1])]
            if current < target:
                i += 1
            else:
                j -= 1