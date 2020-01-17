x=int(input())

def aa(e):
    a = 1
    c = 0
    d = 0
    count=1
    while True:
        for i in range(2):
            c = c + a
            if (d + 1 <=e<=c):
                return count
            d = c
            count=count+1
        a = a + 1

for i in range(x):
    a,b=map(int,input().split())
    print(aa(b-a))






