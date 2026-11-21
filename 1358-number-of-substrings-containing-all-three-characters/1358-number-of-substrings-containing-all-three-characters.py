class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # brute force approach

        # res = 0
        # for i in range(len(s)):
        #     num_set = set()
        #     for j in range(i, len(s)):
        #         num_set.add(s[j])
        #         if len(num_set) == 3:
        #             count = len(s) - j
        #             res += count
        #             break

        # return res

        # optimal approach

        last_seen = [-1, -1, -1]
        res = 0

        for i in range(len(s)):
            last_seen[ord(s[i]) - ord('a')] = i

            res += 1 + min(last_seen)


        return res
        