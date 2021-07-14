import java.util.Arrays;

import javax.swing.Box;
//O(n^2)动态规划,
// 题目要求在3个维度（宽度 + 深度 + 高度）上整体严格递增。
// 先排序1个维度（宽度），先保证在1个维度上递增（并非严格递增）。
// 之后专心处理剩余的2个维度（深度 + 高度）即可，而这就需要使用动态规划。
class Solution_box {
    public int pileBox(int[][] box) {
        int len = box.length;//箱子个数
        Arrays.sort(box, (a, b) -> a[0] == b[0] ? b[1] - a[1] : a[0] - b[0]);
        //(a, b) -> a[0] == b[0] ? a[1] == b[1] ? b[2] - a[2] : b[1] - a[1] : a[0] - b[0] 
        //先按宽度排序，为什么其他两个会降序,降序主要是为了宽度相同的时候也不叠放在一起(因为后面缺少对宽度的条件判断);
        int[] dp_val = new int[len];
        dp_val[0] = box[0][2];//先拿出宽度（或深度）最小箱子，最有可能存在于dp中，
        int res = dp_val[0];
        for (int i = 1; i < len; ++i) {//基地不断扩大，遍历所能叠放的上层子箱子，每个dp[i]都对应最优解！
            int max_val = 0, base_depth = box[i][1], base_height = box[i][2];//这里的max_val若直接取作height会影响子子箱子的选取，应先置零
            for (int j = 0; j < i; ++j)//满足宽度的条件下，按照深度和宽度选取
                if (base_depth > box[j][1] && base_height > box[j][2])
                    max_val = Math.max(max_val, dp_val[j]); //dp[i]以箱子i为基底能取到的最大高度（满足高度和深度的条件下）
            dp_val[i] = max_val + base_height;//二次遍历，对于当前i，找j（即宽度更小的箱子），如果发现深度合适，并且高度小于
            res = Math.max(res, dp_val[i]);
        }
        return res;
    }
}

// print(Solution_box.pileBox(box))
