class Solution:

    def count(self, N):
        self.cache = {0: 0, 1: 1, 2: 2, 3: 4}
        if N in self.cache.keys():
            return self.cache[N]

        for x in range(N):
            self.cache[x] = self.count(
                x-3) + self.count(x-2) + self.count(x-1)

        return self.cache[N]


obj = Solution()
print(obj.count(5))


# class Solution:
#     def fib(self, N: int) -> int:
#         if N <= 1:
#             return N
#         self.cache = {0: 0, 1: 1}
#         return self.memoize(N)

#     def memoize(self, N: int) -> {}:
#         if N in self.cache.keys():
#             return self.cache[N]
#         self.cache[N] = self.memoize(N-1) + self.memoize(N-2)
#         return self.memoize(N)
