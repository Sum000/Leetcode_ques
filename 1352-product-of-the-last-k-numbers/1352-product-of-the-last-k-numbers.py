class ProductOfNumbers:

    def __init__(self):
        self.prefix_prod = [1]
        

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_prod = [1]
        else:
            self.prefix_prod.append(self.prefix_prod[-1] * num)

        

    def getProduct(self, k: int) -> int:
        # brute force approach O(k)
        # res = 1
        # n = len(self.arr)
        # for i in range(n - 1, n - k - 1, -1):
        #     res *= self.arr[i]

        # return res
        if k >= len(self.prefix_prod):
            return 0

        return self.prefix_prod[-1] // self.prefix_prod[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)