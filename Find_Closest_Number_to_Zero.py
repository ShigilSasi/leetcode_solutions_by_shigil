class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_value = nums[0]
        for num in nums:
            if abs(num) < abs(closest_value):
                closest_value = num


        if closest_value < 0 and abs(closest_value) in nums:
            return abs(closest_value)
        else:
            return closest_value
        