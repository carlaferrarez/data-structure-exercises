class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        size_nums = len(nums)
        j = - n
        k = 0
        array = [0] * (size_nums)
        for i in range(size_nums):
            if (i == 0 or i % 2 == 0):
                array[i] = nums[n + j]
                j = j + 1
            else:
                 array[i] = nums[n + k]
                 k = k + 1
        return array