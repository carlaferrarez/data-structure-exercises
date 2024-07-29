class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # nums.sort()
        # if (nums[0] > 0 or nums[len(nums) - 1] < 0):
        #     return len(nums)
        neg = 0
        pos = 0
        for i in range(len(nums)):
            if (nums[i] < 0):
                neg = neg + 1
            elif (nums[i] > 0):
                pos = pos + 1
            else:
                pass
        return max(neg, pos)