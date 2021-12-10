m,n=3,4
dp1=[[0]*n]*m #浅拷贝
#依次赋值深拷贝，python二维数组；
dp2=[[0 for _ in range(n)] for _ in range(m)]
dp3=[[0] * n for _ in range(m)]
dp1[0][2]=3
dp2[0][2]=3
dp3[0][2]=3
print('dp1',dp1)
print('dp2',dp2)
print('dp3',dp3)