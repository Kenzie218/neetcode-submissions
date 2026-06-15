class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0

        while(k != len(nums)):
            if val == nums[k]:
                nums.remove(val)
            else:
                k += 1

        return k