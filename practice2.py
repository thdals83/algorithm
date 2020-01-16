a,b,c=map(int,input().split())

n=(c-b)/(a-b)
if(n==int(n)):
    print(int(n))
else:
    print(int(n)+1)

