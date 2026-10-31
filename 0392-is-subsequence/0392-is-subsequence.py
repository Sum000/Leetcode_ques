class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ch_index = 0
        n = len(s)
        for ch in t:
            if ch_index == n:
                return True
            
            if s[ch_index] == ch:
                ch_index += 1

        if ch_index == n:
            return True
        else:
            return False        