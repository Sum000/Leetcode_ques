class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # brute force approach

        if len(s1) > len(s2):
            return False

        s1_freq = [0] * 26

        for c in s1:
            s1_freq[ord(c) - ord('a')] += 1


        s2_freq = [0] * 26
        k = len(s1)

        for ch in s2[:k]:
            s2_freq[ord(ch) - ord('a')] += 1

        if s1_freq == s2_freq:
            return True

        
        for right in range(k, len(s2)):
            left_char = s2[right - k]
            s2_freq[ord(left_char) - ord('a')] -= 1

            right_char = s2[right]
            s2_freq[ord(right_char) - ord('a')] += 1

            if s1_freq == s2_freq:
                return True

        return False
            





        