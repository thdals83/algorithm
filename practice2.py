def fibo(x):

    if(x<=1):return x
    else:return fibo(x-1)+fibo(x-2)

if __name__=="__main__":
    x=int(input())
    print(fibo(x))