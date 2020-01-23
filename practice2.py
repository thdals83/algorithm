z = 10001
list = [False, False] + [True] * (z - 1)
for i in range(2, z + 1):
    if list[i] == True:
        for j in range(2 * i, z + 1, i):
            list[j] = False

count=int(input())
for _ in range(count):
    x = int(input())
    y=x//2
    for j in range(y,1,-1):
        if(list[x-j]==True and list[j]==True):
            print(j,x-j)
            break
