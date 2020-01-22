def confirm(x,y):

    list=[False,False]+[True]*(y-1)
    index=[]

    for i in range(2,y+1):
        if list[i]==True:
            index.append(i)
            for j in range(2 * i, y + 1, i):
                list[j] = False

    for i in range(x,y+1):
        if(list[i]==True):
            print(i)

if __name__=="__main__":
    x,y=map(int,input().split())
    confirm(x,y)
