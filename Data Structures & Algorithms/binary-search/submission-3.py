class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left = 0
        right = len(nums)-1

        while left <= right:
            middle = (right-left)//2 + left
            number = nums[middle]
            if number == target:
                return middle
            elif number < target:
                left = middle + 1
            elif number > target:
                right = middle - 1


        return -1 