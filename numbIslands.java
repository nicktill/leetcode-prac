class Solution {
  void dfs(char[][] grid, int r, int c) {
    int row = grid.length;
    int column = grid[0].length;

    if (r < 0 || c < 0 || r >= row || c >= column || grid[r][c] == '0') {
      return;
    }
    //classic DFS, calling search on all possible options
    //return th
    grid[r][c] = '0';
    dfs(grid, r - 1, c);
    dfs(grid, r + 1, c);
    dfs(grid, r, c - 1);
    dfs(grid, r, c + 1);
  }

  public int numIslands(char[][] grid) {
    if (grid == null || grid.length == 0) {
      return 0;
    }

    int row = grid.length;
    int column = grid[0].length;
    int numIslands = 0;
    for (int r = 0; r < row; ++r) {
      for (int c = 0; c < column; ++c) {
        if (grid[r][c] == '1') {
          numIslands++;
          dfs(grid, r, c);
        }
      }
    }

    return numIslands;
  }
}
