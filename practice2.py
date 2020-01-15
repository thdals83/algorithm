num=int(input())

i=1
a=0
while True:
    b=a+i
    if(a<num<=b):break
    i=i+1
    a=b

a=a+1
mo=num-a+1
ja=i-mo+1

if(i%2==0):
    print("%d/%d" % (mo, ja))
else:
    print("%d/%d" % (ja, mo))