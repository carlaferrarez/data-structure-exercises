class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negatives = self.countNegatives(nums)
        positives = self.countPositives(nums)
        return max(negatives, positives)

    def countNegatives(self, nums: List[int]) -> int:
        mid = len(nums)//2
        left = 0
        right = len(nums) - 1
        while (right >= left):
            if (nums[mid] >= 0):
                right = mid - 1
            else:
                left = mid + 1
            mid = (right + left) // 2
        count = right
        return count + 1

    def countPositives(self, nums: List[int]) -> int:
        mid = len(nums)//2
        left = 0
        right = len(nums) - 1
        while (right >= left):
            if (nums[mid] <= 0):
                left = mid + 1
            else:
                right = mid - 1
            mid = (right + left) // 2
        count = len(nums) - left
        return count