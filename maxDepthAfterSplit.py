#  A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

# It is the empty string, or
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:

# depth("") = 0
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.
#LC Med, https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings

 
 def maxDepthAfterSplit(self, seq):
        seq = list(seq)
        depth = 1; 
        dictionary = []
        for x in seq:
            if x == '(': #increment depth 
                depth+= 1 
            dictionary.append(depth%2) 
            if x != '(':
                depth-=1 #depth =1
        
        return dictionary