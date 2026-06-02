class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = defaultdict(list)
        nums.sort()

        for i in range(len(nums)):
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while(left < right):
                total = nums[left] + nums[right]
                
                if total < target:
                    left += 1

                elif total > target:
                    right -= 1

                else:
                    t_sorted = tuple([nums[left], nums[i], nums[right]])
                    if t_sorted not in result:
                        result[t_sorted] = [nums[i], nums[left], nums[right]]

                    left += 1
                    right -= 1

        return list(result.values())