class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        l = len(num)
        if l == k:
            return "0"
        stack.append(num[0])
        for i in range(1, l):     
            while stack and num[i] < stack[-1] and k > 0:
                stack.pop()
                k = k - 1
            stack.append(num[i])
            
        while stack and stack[0] == "0":
            stack.pop(0)
            
        while stack and k > 0:
            stack.pop()
            k -= 1
            
         
                
        res = "".join(stack)
        return res if res else "0"
        
        
        