class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        max_prof = 0
        cur_price = 0
        right = 0

        while(right != len(prices)):
            cur_price = prices[left]
            profit = prices[right] - cur_price

            if(profit < 0):
                left += 1

            else:
                max_prof = max(max_prof, profit)
                right += 1

        return max_prof