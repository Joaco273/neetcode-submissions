class Solution:
    def search(self, nums: List[int], target: int) -> int:
        totalLength = len(nums)
        left = 0
        right = totalLength-1

        if totalLength == 1:
            if nums[0] == target:
                return 0
        

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1