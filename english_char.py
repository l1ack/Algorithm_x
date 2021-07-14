#  //	取整除 - 返回商的整数部分（向下取整）
class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def helper(num):
            if num < 20:
                return to19[num - 1:num]
            if num < 100:
                return [tens[num // 10 - 2]] + helper(num  % 10)
            if num < 1000:
                return [to19[num // 100 - 1]] + ['Hundred'] + helper(num % 100)
            for p, w in enumerate(['Thousand', 'Million', 'Billion'], 1):
                print(p)
                #第一次得到的数是324882，第二次得到的数是324此时p=2，如果不小于1000的p+1幂次方，则p+1，直到3得到billion；先取整，再取余
                if num < 1000 ** (p + 1):
                    # print(helper(num // 1000 ** p))
                    # print(helper(num % 1000 ** p))
                    return helper(num // 1000 ** p) + [w] + helper(num % 1000 ** p)
        return ' '.join(helper(num)) or 'Zero'
#666 777 888 W 999 1
#666 777 W 888 999 2
#666 w 777 888 999 p=3的时候取整数,余数为777 888 999 这时候取余的函数需要取整，此时p为1，重新开始，直到p=2，找到取整（777），888 999可以直接取余取整，此时递归结束，返回余数和整数组合，此时

num=666777888999#666 777 888 999
print(Solution.numberToWords(Solution,num))
