import numpy
class Solution:
    def numTrees(self, n: int) -> int:
        a =  numpy.math.factorial(2*n)
        b = numpy.math.factorial(n)
        x = b * b * (n + 1)
        return a // x
        