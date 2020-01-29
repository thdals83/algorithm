def make(i,j):
    while(i!=0):
        if (i % 3 == 1 and j % 3 == 1):
            print(" ", end="")
            return None
        i=i//3
        j=j//3
    print("*", end="")


if __name__=="__main__":
    x=int(input())
    for i in range(0,x):
        for j in range(0,x):
            make(i,j)
        print("")
