class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # max_len = 0
        # for i in range(len(s)):
        #     freq_arr = [0] * 26
        #     max_freq = 0
        #     for j in range(i, len(s)):
        #         index = ord(s[j]) - ord('A')
        #         freq_arr[index] += 1
        #         max_freq = max(max_freq, freq_arr[index])
        #         changes = (j - i + 1) - max_freq

        #         if changes <= k:
        #             max_len= max(max_len, j - i + 1)
        #         else:
        #             break

        # return max_len

        # optimal solution 

        max_len = 0
        l, r = 0, 0
        freq_arr = [0] * 26

        while r < len(s):
            index = ord(s[r]) - ord('A')
            freq_arr[index] += 1

            max_freq = max(freq_arr)

            while (r - l + 1) - max_freq > k:
                left_index = ord(s[l]) - ord('A')
                freq_arr[left_index] -= 1
                l += 1

                max_freq = max(freq_arr)

            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len


                




        