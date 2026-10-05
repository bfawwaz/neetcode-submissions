class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        x = {z: 0 for z in s}
        h = {b: 0 for b in t}
        for f in t:
            h[f] += 1
        for i in s:
            x[i] += 1
        
        print(x)
        print(h)
        if x != h:
            return False
        return True
