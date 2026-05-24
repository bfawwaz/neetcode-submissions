class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        frequencies = {n:1 for n in nums}
        print(frequencies)
        i = 0
        result = []
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                frequencies[nums[i]] += 1  
            i += 1
        sorted_desc = dict(sorted(frequencies.items(), key=lambda item: item[1], reverse=True))

        print(sorted_desc)
        print(list(sorted_desc.keys())[0])
        for x in range(k):
            result.append(list(sorted_desc.keys())[x])
        return result




        #     I go through the array first time
        #     I start with the first element
        #     I know what it is
        #     I go to its neighbor and compare it with it
        #     if its the same I incrememnt that numbers frequency by 1
        #     if not 
        #     then I move to the next element
        #     if its neighbor is the same 
        #     then I incrememnert its frequency by 1
        #     then go to next element asnd check if even its neighbor is the same
        #     if yes incrememnt by 1
        #     keep doing that until I hit a new element
        #     then I start checking the new elements neighbor 
            
