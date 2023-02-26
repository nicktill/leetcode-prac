class Solution(object):
    def generateParenthesis(self, n):
        # Define a helper function for the depth-first search (DFS) algorithm
        def dfs(left, right, s):
        #if length 2*n, its valid parentheses, so add it to the results list and return
            if len(s) == n * 2:
                res.append(s)
                return
            # If we haven't used all n left parentheses yet, add one to the string s and continue the DFS
            if left < n:
                dfs(left + 1, right, s + '(')
            # If we've used more left than right parentheses, add a right parentheses to the string s and continue the DFS
            if right < left:
                dfs(left, right + 1, s + ')')

        # Initialize an empty list to hold the results
        res = []
        # Call the DFS function with initial values of 0 for left and right parentheses, and an empty string for the current string s
        dfs(0, 0, '')
        # Return the list of valid parentheses strings
        return res
