def confirm(x,y):

    list=[False,False]+[True]*(y-1)
    index=[]
    count=0
    for i in range(2,y+1):
        if list[i]==True:
            index.append(i)
            for j in range(2 * i, y + 1, i):
                list[j] = False

    for i in range(x+1,y+1):
        if(list[i]==True):
            count=count+1

    print(count)

if __name__=="__main__":
    while True:
        x=int(input())
        y=2*x
        if(x==0):break
        confirm(x,y)
