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

    return False

if __name__=="__main__":
    x=int(input())
    if(confirm(x)):print("소수입니다.")
    else:print("소수가 아닙니다.")
