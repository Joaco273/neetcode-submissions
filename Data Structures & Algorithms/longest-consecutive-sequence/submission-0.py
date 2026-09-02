class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setOfNums = set(nums)
        currentLength = 0
        maximumLength = 0
        for number in setOfNums:
            if number-1 not in setOfNums:
                currNum = number
                currentLength = 1

                while currNum + 1 in setOfNums:
                    currNum += 1
                    currentLength += 1
                maximumLength = max(maximumLength, currentLength)
        
        return maximumLength