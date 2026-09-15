class Solution:
    def maxArea(self, heights: List[int]) -> int:
        totalArea = 0
        leftIndex = 0
        rightIndex = len(heights) - 1



        while leftIndex < rightIndex:
            area = (rightIndex - leftIndex) * min(heights[leftIndex], heights[rightIndex])
            if area > totalArea:
                totalArea = area
            leftVal = heights[leftIndex]
            rightVal = heights[rightIndex]
            if leftVal < rightVal:
                leftIndex += 1
            else:
                rightIndex -= 1
            
        return totalArea

