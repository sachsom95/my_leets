# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

def count_steps(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return count_steps(n-3)+count_steps(n-2)+count_steps(n-1)


class Solution:

    def dp(self, N):
        if N in self.cache.keys():
            return self.cache[N]
        self.cache[N] = self.dp(
            N-3) + self.dp(N-2) + self.dp(N-1)
        return self.cache[N]

    def count_step_dp(self, N):
        self.cache = {0: 0, 1: 1, 2: 2, 3: 4}

        return self.dp(N)


obj = Solution()
z = 10
print(count_steps(z))
print(obj.count_step_dp(z))
