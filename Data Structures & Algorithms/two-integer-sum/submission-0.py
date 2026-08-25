class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenSums = {}
        index = 0
        for number in nums:
            complement = target - number
            if (number in seenSums):
                return [seenSums[number], index]
            else:
                seenSums[complement] = index
                index += 1