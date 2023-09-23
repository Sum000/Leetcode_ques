class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        
        for num in tokens:
            if num == "+" or num == "-" or num == "*" or (num == "/" and stack):
                right = int(stack.pop())
                left = int(stack.pop())
                
                if num == "+":
                    res = left + right
                elif num == "-":
                    res = left - right
                elif num == "*":
                    res = left * right
                else:
                    res = int(left / right)
                    
                stack.append(res)
            else:
                stack.append(int(num))
                
        return stack[0]
                
    
                
     
                
                