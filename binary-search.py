class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        half = (len(nums))//2
        if (target == nums[half]):
            return half
        while(right >=left):
            if  (target == nums[half]):
                return half
            elif (target > nums[half]):
                left = half + 1
                half = (right +left ) // 2 
            else:
                right = half - 1
                half = (right + left) // 2 
        return - 1