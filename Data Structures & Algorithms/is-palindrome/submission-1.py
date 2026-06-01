class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_s = ''.join(filter(str.isalnum, s)).lower() #removed spaces and non-alpha letters

        i = 0
        j = len(new_s) - 1

        for i in range(len(new_s)):
            if new_s[i] != new_s[j]:
                return False
            j -= 1
        return True