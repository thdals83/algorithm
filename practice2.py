x,y,w,h=map(int,input().split())

q=w-x
e=h-y

print(min(x,y,q,e))