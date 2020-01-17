arr=[[0]*14 for i in range(15)]

for i in range(14):
    arr[0][i]=i+1
    arr[i][0]=1
arr[14][0]=1

for i in range(1,15):
    for j in range(1,14):
        arr[i][j]=arr[i][j-1]+arr[i-1][j]


t=int(input())
for i in range(t):
    a = int(input())
    b = int(input())
    print(arr[a][b-1])






