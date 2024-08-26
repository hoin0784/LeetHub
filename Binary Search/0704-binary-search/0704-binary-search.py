class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1       # l = 0 , r = 5

        while l <= r:
            center = (l + r) //2

            if nums[center] < target:     
                l = center + 1      
            elif nums[center] > target:
                r = center - 1
            else:
                return center
        return -1
            

        
        