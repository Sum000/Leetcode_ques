class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # brute force approach
        # res = 0
        # for i in range(len(fruits)):
        #     fruit_set = set()
        #     for j in range(i, len(fruits)):
        #         fruit_set.add(fruits[j])
        #         if len(fruit_set) <= 2:
        #             res = max(res, j - i + 1)
        #         else:
        #             break


        # return res

        # optimal approach

        # max_len = 0
        # l, r = 0, 0

        # freq_map = {}
        # k = 2

        # while r < len(fruits):

        #     freq_map[fruits[r]] = freq_map.get(fruits[r], 0) + 1

        #     while len(freq_map) > k:

        #         freq_map[fruits[l]] -= 1

        #         if freq_map[fruits[l]] == 0:
        #             freq_map.pop(fruits[l])

        #         l += 1

        #     max_len = max(max_len, r - l + 1)

        #     r += 1

        # return max_len


        # most optimal solution

        l, r = 0, 0
        max_len = 0
        k = 2
        freq_map = {}

        while r < len(fruits):

            freq_map[fruits[r]] = freq_map.get(fruits[r], 0) + 1

            if len(freq_map) > k:
                freq_map[fruits[l]] -= 1

                if freq_map[fruits[l]] == 0:
                    freq_map.pop(fruits[l])

                l += 1
            else:
                max_len = max(max_len, r - l + 1)

            r += 1

        return max_len



                    
        