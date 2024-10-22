class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = { ')':'(', ']':'[','}':'{'}
        for x in s:
            if x in brackets.values():
                stack.append(x)
            elif x in brackets:
                if stack and stack[-1] == brackets[x]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        else: 
            return True