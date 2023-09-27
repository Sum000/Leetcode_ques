class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        stack.append(int(operations[0]))
        
        n = len(operations)
        
        for i in range(1, n):
            if operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                stack.append(2 * stack[-1])    
            elif operations[i] == "+":
                stack.append(stack[-1] + stack[-2])   
            else:
                stack.append(int(operations[i]))
        
            
        return sum(stack)
            
            
        
        