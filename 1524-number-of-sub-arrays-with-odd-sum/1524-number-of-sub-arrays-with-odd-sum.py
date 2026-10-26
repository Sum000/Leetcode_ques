class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        # brute force approach

        # total, res = 0, 0
        # for i in range(len(arr)):
        #     total += arr[i]
        #     if total % 2 == 1:
        #         res += 1
        #     for j in range(i + 1, len(arr)):
        #         total += arr[j]
        #         if total % 2 == 1:
        #             res += 1
        #     total = 0
        # return res

        # optimal approach

        total, res, odd, even = 0, 0, 0, 1

        for n in arr:
            total += n 
            if total % 2 == 1:
                res += even
                odd += 1
            else:
                res += odd
                even += 1
        
        mod = 10**9 + 7
        res = res % mod
        return res


        