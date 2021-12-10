import java.util.Scanner;

public class changechar {
        public static int minFlipsMonoIncr(String s) {
    //0不能出现在1后面;
    //翻转前面还是反转后面
    //找到逆序对;
    //对于每一个数，记录前面为1，记录后面为0的dp
            int len=s.length();
            int min=len;
            int[][] dp=new int[len][2];
            if (s.charAt(0)=='1')dp[0][1]=1;
            if (s.charAt(len-1)=='0')dp[len-1][0]=1;
            for(int i=1;i<len;i++){
                if (s.charAt(i)=='1')
                dp[i][1]=dp[i-1][1]+1;
                else dp[i][1]=dp[i-1][1];
                System.out.println(dp[i][1]);
            }
            for(int i=len-2;i>=0;i--){
                if (s.charAt(i)=='0')
                dp[i][0]=dp[i+1][0]+1;
                else dp[i][0]=dp[i+1][0];
            }
            for(int i=0;i<len;i++){
                dp[i][0]=dp[i][0]+dp[i][1];
                min=Math.min(dp[i][0],min);
            }
            return min-1;
        }
        public static void main(String[] args){
            try (Scanner input = new Scanner(System.in)) {
                String str = input.next();
                // str="11111110000000000";
                System.out.println(minFlipsMonoIncr(str));
            }
        }
}
