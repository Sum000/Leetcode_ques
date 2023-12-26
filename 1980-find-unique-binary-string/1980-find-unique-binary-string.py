class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        
        def backtrack(cur):
            if n == len(cur):
                if cur not in nums:
                    return cur
                
                return ""
            
            add_zero = backtrack(cur + "0")
            if add_zero:
                return add_zero
            
            return backtrack(cur + "1")
        
        return backtrack("")
        