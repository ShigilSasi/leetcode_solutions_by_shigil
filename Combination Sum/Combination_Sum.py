class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        nums = candidates
        n = len(nums)

        def backtrack(i, cur_summ):
            if target == cur_summ:
                res.append(sol[:])
                return

            if target < cur_summ or i == n:
                return

            backtrack(i + 1, cur_summ)
            sol.append(nums[i])
            backtrack(i, cur_summ + nums[i])
            sol.pop()

        backtrack(0, 0)
        return res