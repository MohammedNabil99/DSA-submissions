class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # addition = {}
        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in addition:
        #         return [addition[diff], i]
        #     addition[n] = i 
        prevMap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[nums[i]] = i
        