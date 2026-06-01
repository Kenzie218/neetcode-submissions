class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     difference = target - nums[i]

        #     if difference in nums:
        #         index_j = nums.index(difference)
        #         if i != index_j:
        #             return sorted([i, index_j])

        #Optimized Solution
        HashMap = {} #val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in HashMap:
                return [HashMap[diff], i]
            HashMap[n] = i
        return []