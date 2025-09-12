class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1

        if len(s) != len(t):return False

        for c in t:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]  
            else:
                counter[c] -= 1

        return True
        