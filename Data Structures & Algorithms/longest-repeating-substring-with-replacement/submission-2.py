class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0

        cur_count = {}
        max_freq = 0
        result = 0

        for right in range(len(s)):
            #Increment the current count of a character or create a space for it
            cur_count[s[right]] = 1 + cur_count.get(s[right], 0)

            max_freq = max(cur_count[s[right]], max_freq)

            while(right - left + 1) - max_freq > k:
                cur_count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
            
