a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())

if(a==c and a!=e):x=e
elif(a==e and a!=c):x=c
else:x=a

if(b==d and b!=f):y=f
elif(b==f and b!=d):y=d
else:y=b

print(x,y)