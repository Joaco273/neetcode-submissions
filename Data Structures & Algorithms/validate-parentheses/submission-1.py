class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')':'(', ']':'[', '}':'{'}

        for char in s:
            if char in matching:
                if len(stack)==0:
                    return False
                elif stack.pop() != matching[char]:
                    return False
            else:
                stack.append(char)
        
        return len(stack)==0