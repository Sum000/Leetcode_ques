class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                diff = a + stack[-1]
                
                if diff < 0:
                    stack.pop()
                    continue
                elif diff == 0:
                    stack.pop()
                break
            else:
                stack.append(a)
                
        return stack
        