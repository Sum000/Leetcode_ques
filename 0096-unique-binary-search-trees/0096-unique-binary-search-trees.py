class Solution:
    def numTrees(self, n: int) -> int:
        a =  math.factorial(2*n)
        b = math.factorial(n)
        x = b * b * (n + 1)
        return a // x
        