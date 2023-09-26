class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        m = len(nums1)
        n = len(nums2)
        
        res = [-1] * m
        for i in range(0,m) :
            k = 1
            index = nums2.index(nums1[i])
            while index + k < n:
                if nums1[i] < nums2[index + k]:
                    res[i] = nums2[index + k]
                    break
                k += 1
                
        return res
                
            
        