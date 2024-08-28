class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1        # 0, 3

        while left <= right:
            center = (left + right) // 2    # 1

            if target == nums[center]:
                return center

            elif target > nums[center]:
                left = center + 1
            else:
                right = center -1
        return left    

