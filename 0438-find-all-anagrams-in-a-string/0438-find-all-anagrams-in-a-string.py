class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        len_p = len(p)
        freq_arr_p = [0] * 26
        freq_arr_s = [0] * 26
        l, r = 0, len_p - 1

        for c in p:
            index = ord(c) - ord('a')
            freq_arr_p[index] += 1

        for c in s[:r + 1]:
            index = ord(c) - ord('a')
            freq_arr_s[index] += 1

        if freq_arr_s == freq_arr_p:
            res.append(l)


        l += 1
        r += 1

        while r < len(s):
            prev_index = ord(s[l - 1]) - ord('a')
            freq_arr_s[prev_index] -= 1
            cur_index = ord(s[r]) - ord('a')
            freq_arr_s[cur_index] += 1

            if freq_arr_s == freq_arr_p:
                res.append(l)

            l += 1
            r += 1

        return res




        