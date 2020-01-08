import random

def make_Array():
    list=[[1,1,1,0,0,0],
          [0,1,0,0,0,0],
          [1,1,1,0,0,0],
          [0,0,2,4,4,0],
          [0,0,0,2,0,0],
          [0,0,1,2,4,0]]
    return list

def Plus(a,x,y):
    max=0
    j=y
    for i in range(3):
        max=max+a[x][j]+a[x+2][j]
        j=j+1
    max=max+a[x+1][y+1]
    return max

def compare_Array(arr):
    a=0
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            if(a==0):
                max=Plus(arr,i,j)
                tmp=max
                a=1
            max = Plus(arr, i, j)
            if(tmp<max):
                tmp=max

    return tmp

if __name__=="__main__":
    list=make_Array()
    maximum=compare_Array(list)

    print(maximum)
