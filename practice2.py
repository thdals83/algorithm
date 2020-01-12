def confirm(x):
    global count
    count=0

    list=[False,False]+[True]*(x-1)
    index=[]

    for i in range(2,x+1):
        count=count+1
        if list[i]:
            index.append(i)
            for j in range(2*i,x+1,i):
                if(x==j):return False
                list[j]=False
    return True

if __name__=="__main__":
    x=int(input())
    if(confirm(x)):print("소수입니다.")
    else:print("소수가 아닙니다.")
    print(count)
