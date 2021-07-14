import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class Solution {
//DFS 基于迭代 
//BFS 基于队列 BSF树
private List<List<String>> res = new ArrayList<>();

public List<List<String>> solveNQueens(int n) {
        char [][]grid = new char[n][n];
        for (int i=0; i < n; i++){
            for (int j=0;j<n; j++){
                grid[i][j]='.';
            }
        }//初始化
        boolean[] col = new boolean[n];
        boolean[] dg = new boolean[n+n];
        boolean[] udg = new boolean[n+n];
        dfs(0,n,grid,col,dg,udg);//从0行开始

        return res;
    }

private void dfs(int h, int n, char[][] grid, boolean[] col,boolean[] dg,boolean[] udg){
    if(h == n) {
        List<String> list = new ArrayList<>();
        for(int i=0;i < grid.length; i++){
            list.add(new String(grid[i]));//逐行添加
        }
        res.add(list);
        return;
    }
    for(int j=0;j<n;j++){
        if(!col[j] && !dg[n-h+j]&& !udg[h+j]){
            grid[h][j]='Q';
            col[j]=dg[n-h+j]=udg[h+j]=true;
            dfs(h+1,n,grid,col,dg,udg);//找到所有为true的，其余递归置'.'
            grid[h][j]='.';
            col[j]=dg[n-h+j] = udg [h+j]=false;
        }
    }
}
}
// print(Solution.solveNQueens(8))



//基于位运算的回溯
class Solution_weiyunsuan {
    public List<List<String>> solveNQueens(int n) {
        int[] queens = new int[n];
        Arrays.fill(queens, -1);
        List<List<String>> solutions = new ArrayList<List<String>>();
        solve(solutions, queens, n, 0, 0, 0, 0);
        return solutions;
    }

    public void solve(List<List<String>> solutions, int[] queens, int n, int row, int columns, int diagonals1, int diagonals2) {
        if (row == n) {
            List<String> board = generateBoard(queens, n);
            solutions.add(board);
        } else {
            int availablePositions = ((1 << n) - 1) & (~(columns | diagonals1 | diagonals2));
            while (availablePositions != 0) {
                int position = availablePositions & (-availablePositions);
                availablePositions = availablePositions & (availablePositions - 1);
                int column = Integer.bitCount(position - 1);
                queens[row] = column;
                solve(solutions, queens, n, row + 1, columns | position, (diagonals1 | position) << 1, (diagonals2 | position) >> 1);
                queens[row] = -1;
            }
        }
    }

    public List<String> generateBoard(int[] queens, int n) {
        List<String> board = new ArrayList<String>();
        for (int i = 0; i < n; i++) {
            char[] row = new char[n];
            Arrays.fill(row, '.');
            row[queens[i]] = 'Q';
            board.add(new String(row));
        }
        return board;
    }
}
