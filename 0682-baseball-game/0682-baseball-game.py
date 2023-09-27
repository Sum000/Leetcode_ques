class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        stack.append(int(operations[0]))
        
        n = len(operations)
        
        for i in range(1, n):
            if operations[i] == "+":
                new_score = stack[-1] + stack[-2]
                stack.append(new_score)
            elif operations[i] == "D":
                new_score = 2 * stack[-1]
                stack.append(new_score)
                
            elif operations[i] == "C":
                if stack:
                    stack.pop()
                    
            else:
                stack.append(int(operations[i]))
                
        sum = 0
        
        for num in stack:
            sum += num
            
        return sum
            
            
        
        