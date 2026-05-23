class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = sorted([c for c in s])
        second = sorted([c for c in t])
        if first == second:
            return True
        return False