class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a hashmap with keys being whawtever is in nums, values as 0
        #value will act as the number of times we have seen the element in nums
        #loop over nums
        #for every number, increase the value of its key by 1
        #if anything goes over 1, its a duplicate

        hash_of_nums = {x: 0 for x in nums}
        for num in nums:
            hash_of_nums[num] += 1
            if hash_of_nums[num] > 1:
                return True
        return False