class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        prefix = [0] * numsLen
        sufix = [0] * numsLen
        returnableList = [0] * numsLen

        for i in range(numsLen):
            if i > 0:
                prefix[i] = nums[i-1] * prefix[i-1]
            else:
                prefix[i] = 1
        
        for i in reversed(range(numsLen)):
            if i < numsLen-1:
                sufix[i] = nums[i+1] * sufix[i+1]
            else:
                sufix[i] = 1
        

        for i in range(numsLen):
            returnableList[i] = sufix[i] * prefix[i]
        
        return returnableList

