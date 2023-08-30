class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op = 0
        n = len(nums)
        
        for i in range(n - 2, -1, -1):
            
            if nums[i] <= nums[i + 1]:
                continue
                
            num_elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
            
            op += num_elements - 1
            
            nums[i] = nums[i] // num_elements
            
            
        return op
                
        
      
        