class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        max_count = -1
        val = -1

        for key, value in counter.items():
            if value > max_count:
                max_count = value
                val = key


        return val
        