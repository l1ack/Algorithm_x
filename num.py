class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        #动态规划 时间复杂度o(n),空间o(n);
        #找素数       
        #不是个数而是次数；
        #按位来划分
        s=0
        dp = [0 for _ in range(n+1)]
        dp[2]=1
        for num in range(n+1):
            # print(num)
            p=len(str(num))
            # print(p)
            if ((num//10**(p-1))==2 ):
                dp[num]=dp[num % 10 ** (p-1)]+1
            else: 
                dp[num]=dp[num % 10 ** (p-1)]
            # print(num % 10 ** (p-1))
            # print("fefwefw")
            # print(dp[num])
            # print("fhuiarharu")
            if(dp[num]!=0):print(num)
            s+=dp[num]
        print(s)
    
Solution.numberOf2sInRange(Solution,1125)

