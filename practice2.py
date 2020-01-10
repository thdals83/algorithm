import random
import queue

def made(x):
    arr=[]
    for i in range(x): arr.append(random.randint(1,300))
    return arr

def radix_sort(list,n):
    baskets=[]
    tmp=0
    factor=1
    for i in range(10): baskets.append(queue.Queue()) #10인 이유는 0~9까지의 버킷

    for i in range(4): #4인이유는 일단 4개의 자리수 칸들
        for j in range(n):
            x=int((list[j]//factor)%10)
            baskets[x].put(list[j])

        for k in range(10):
            while baskets[k].empty()==False:
                if tmp>n-1: tmp=0
                list[tmp]=baskets[k].get()
                tmp=tmp+1
        factor=factor*10

    list.reverse()
    print(list)


if __name__=="__main__":
    x = int(input("개수 입력:"))
    input=made(x)
    print(input)
    radix_sort(input,x)