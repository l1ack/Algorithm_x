class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        s= str(n) 
        x= 2
        count = 0
        for i in range(len(s)):
            current = int(s[i])
            high = 0 if s[:i]=='' else int(s[:i]) 
            print(high)
            low = 0 if s[i+1:]=='' else int(s[i+1:])
            print(low)
            if current>x:
                count+=(high+1)*(10**len(s[i+1:]))
                #print(count)
            elif current<x:
                count += (high) * (10 ** len(s[i + 1:]))
                #print(count)
            else:
                count +=(high) * (10 ** len(s[i + 1:]))+low+1
                #print(count)
        print(count)
        # print(1457+1300+1250+1246)
        return count

Solution.numberOf2sInRange(Solution,12456)