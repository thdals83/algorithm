x=int(input())

i=1
while True:
    a=1
    b=3*i*(i-1)+2
    if(a<=x<b):
        print(i)
        break
    a=b
    i=i+1