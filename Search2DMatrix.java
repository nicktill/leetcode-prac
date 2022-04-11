class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length-1;  //start from last row and first column
        int col = 0;
        
        while(col < matrix[0].length && row>= 0)
        {
            //if greater than target decrement rows
            if(matrix[row][col] > target) row--;
            
            //if less than target increase columns
            else if(matrix[row][col]<target) col++;
            
            else return true; //otherwise return true because it is equal if not great or less
        }
        //otherwise, break outside since could not find target value
        return false;
    }
}
