#https://leetcode.com/problems/zigzag-conversion/submissions/
#this has to be the worst one
class Solution(object):
    def convert(self, s, numRows):
        if numRows is None: 
            return ''
        if numRows == 1:
            return s
        rows = [''] * numRows
        row = 0
        goingDown = False
        for c in s:
            rows[row] += c

            if goingDown and row == numRows -1: 
                goingDown = False 
            if not goingDown and row == 0: 
                goingDown = True 
            
            if goingDown:
                row+=1
            if not goingDown: 
                row-=1 
            
        return "".join(rows)

