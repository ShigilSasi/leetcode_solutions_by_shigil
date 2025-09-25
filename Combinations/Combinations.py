class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])
                return

            left = x
            still_needed = k - len(sol)

            if left > still_needed:
                backtrack(x - 1)

            sol.append(x)
            backtrack(x - 1)
            sol.pop()

        backtrack(n)
        return res        