class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1}
        zero, one, max_len = 0, 0, 0
        
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                zero += 1
            else:
                one += 1
                
            diff = zero - one
            
            if diff in count_map:
                max_len = max(max_len, i - count_map[diff])
            else:
                count_map[diff] = i
                
        return max_len
            
        