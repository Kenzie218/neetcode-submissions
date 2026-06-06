class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """m = len(s) // 2
        left = 0
        right = len(s) - 1
        temp = ""

        for i in range(m):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1"""

            #Better Way

        left = 0
        right = len(s) - 1

        while (left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
