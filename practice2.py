'''
문자열 s를 숫자로 변환한 결과를 반환하는 함수작성
- s의 길이는 1 이상 5이하
- s의 맨앞에는 부호(+, -)가 올 수 있음
- s는 부호와 숫자로만 이루어져있음
- s는 0으로 시작하지 않음
'''

def Change(s):
    n=int(s)
    return n

def Input():
    while True:
        string1 = input("입력:")
        if(string1[0]=='0'):print("다시 입력하세요(첫번재 자리 0으로 시작 불가)")
        elif(1>len(string1) or len(string1)>5):print("다시입력하세요 (문자열길이 1이상 5이하)")
        else:break

    return string1


if __name__=="__main__":
    string=Input()
    print(Change(string))