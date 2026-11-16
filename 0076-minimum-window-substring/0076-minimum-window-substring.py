class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # brute force approach

        # freq_t = [0] * 128

        # for c in t:
        #     freq_t[ord(c)] += 1

        # min_len = float('inf')
        # start_index = -1

        # for i in range(len(s)):
        #     freq = freq_t[:]
        #     count = 0

        #     for j in range(i, len(s)):
        #         index = ord(s[j])

        #         if freq[index] > 0:
        #             count += 1

        #         freq[index] -= 1

        #         if count == len(t):
        #             if j - i + 1 < min_len:
        #                 min_len = j - i + 1
        #                 start_index = i

               
        #             break

        # if start_index == -1:
        #     return ""

        # return s[start_index:start_index + min_len]

        # optimal solution


        l, r = 0, 0
        freq_arr = [0] * 256

        for c in t:
            freq_arr[ord(c)] += 1

        count = 0
        min_len = float('inf')
        start_index = -1

        while r < len(s):   

            right_index = ord(s[r])

            if freq_arr[right_index] > 0:
                count += 1

            freq_arr[right_index] -= 1

            while count == len(t):

                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    start_index = l

                left_index = ord(s[l])
                freq_arr[left_index] += 1

                if freq_arr[left_index] > 0:
                    count -= 1

                l += 1

            r += 1

        if start_index == -1:
            return ""

        return s[start_index:start_index + min_len]


            


            
            

        if start_index == -1:
            return ""


        return s[start_index: start_index + min_len]

        