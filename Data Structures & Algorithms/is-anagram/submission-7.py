class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """sort_s = ''.join(sorted(s))
        sort_t = ''.join(sorted(t))

        if sort_s == sort_t:
            return True
        return False"""

        #Most efficient - count the frequency of each character

        if len(s) != len(t):
            return False

        #The Counter class in the collections library can to count the frequency of elements in an iterable
        return Counter(s) == Counter(t)