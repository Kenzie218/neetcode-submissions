class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}

        #create the hashtable
        for c in s:
            # if c not in hash_s:
            #     hash_s[c] = 1
            # else:
            #     hash_s[c] += 1

            hash_s[c] = hash_s.get(c, 0) + 1

        
        for c in t:
            if c in hash_s:
                hash_s[c] -= 1
            
                if hash_s[c] < 0:
                    return False
            else:
                return False
        
        return True

