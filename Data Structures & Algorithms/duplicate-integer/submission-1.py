class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """unique = []

        for i in range(len(nums)):
            if(nums[i] in unique):
                return True
            else:
                unique.append(nums[i])

        return False"""

        #Optimized Version

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
