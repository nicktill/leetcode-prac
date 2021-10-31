class Solution(object):
    def minRemoveToMakeValid(self, s):
        stack = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = "" #removing extra paranthesis
        for x in stack:   
            s[x] = ""
        return "".join(s)