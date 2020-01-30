import sys
list=list(input().split()) #나라 입력
n=([0]*4) #각 나라의 점수를 만들 리스트 4개

for _ in range(6):
    a, b, x, y, z = input().split() #입력
    x = float(x)
    y = float(y)
    z = float(z)

    for i in range(4): # 입력한 국가와 비교해 승점을 입력해줌
        if(a==list[i]):
            if(y==0):
                n[i] = n[i] + x
            else:
                n[i]=n[i]+((x+y)/2)
        if(b==list[i]):
            if(y==0):
                n[i] = n[i] + z
            else:
                n[i]=n[i]+((y+z)/2)


for i in range(4):  #승점 출력
    print(n[i]/3)

s=sorted(n,reverse=True)


