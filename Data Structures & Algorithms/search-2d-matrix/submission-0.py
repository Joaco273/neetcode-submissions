class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for numbers in matrix:
            if numbers == None:
                pass
            if target < numbers[0]:
                return False
            elif target > numbers[len(numbers) - 1]:
                pass
            else:
                totalLength = len(numbers)
                left = 0
                right = totalLength-1

                if totalLength == 1:
                    if numbers[0] == target:
                        return True
                

                while left <= right:
                    mid = (left + right) // 2

                    if numbers[mid] == target:
                        return True
                    elif numbers[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                        
        return False