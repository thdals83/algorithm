def check(x):
    if(x<2):return False

    for i in range(2,x):
        if(x%i==0):
            return False
    return True

def confirm(x):
    for i in range(x + 1):
        if (check(i) == True):
            if(i==x):return True
    count=0

    return False
    list=[False,False]+[True]*(x-1)
    index=[]

    for i in range(2,x+1):
        if list[i]:
            index.append(i)
            for j in range(2*i,x+1,i):
                if(x==j):return False
                list[j]=False
    return True

if __name__=="__main__":
    x=int(input())
    count=0
    a=list(map(int,input().split()))
    for i in range(len(a)):
        if(confirm(a[i])==True):
            count=count+1

print(count)