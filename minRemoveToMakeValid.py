class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s) #turn string into list so we can iterate through characters
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                if stack: #if stack means that theres a '(' paranthesis added to stack
                    stack.pop() #therefore pop since since found the end paranthesis ')'
                else: #otherwise we have a ')' before a '(' and need to remove it from list
                    s[i] = ""
    
        return "".join(s) #we need to do this to return the list of characters back into a string
       
                    