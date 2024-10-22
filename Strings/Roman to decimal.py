class Solution:
    def romanToInt(self, s: str) -> int:
        r = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        stack = []
        for x in s:
            if stack and r[x] > stack[-1]:
                res += r[x]-stack[-1]
                stack.pop()
            else:
                stack.append(r[x])
        for x in stack:
            res += x
        return res